from html import escape


class Node:
    def __init__(self, document):
        self.doc = document
        self.child_nodes = []
        self.parent_node = document.current_node
        self.parent_node.child_nodes.append(self)
        self.level = self.parent_node.level + 1
        self.index = len(self.parent_node.child_nodes)

    def __enter__(self, **kwargs):
        self.doc.current_node = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.doc.current_node = self.parent_node

    def _is_last(self):
        if self.parent_node:
            return self.index == len(self.parent_node.child_nodes)
        return True

    def append_to(self, node):
        node.child_nodes.append(self)
        return self

    def remove(self):
        self.parent_node.child_nodes.remove(self)


class XmlNode(Node):
    def __init__(self, document, tag_name, content=None, safe=False, attrs={}):
        super().__init__(document)
        self.tag_name = tag_name
        self.attrs = attrs
        self.safe = safe
        self.content = content

    def __repr__(self):
        attrs = ', '.join('{}={}'.format(key, value) for key, value in self.attrs.items())
        return '{}({}{})'.format(self.__class__.__name__, self.tag_name, ', ' + attrs if attrs else '')

    def render(self):
        indent = self.doc.indent
        inner = self.content or ''
        if not self.safe:
            inner = escape(inner, quote=False)
        inner += ''.join([n.render() for n in self.child_nodes])
        html = self.doc.render_tag(self.tag_name, inner, self.attrs)

        if indent:
            pretty_html = '\n' + (indent * self.level) + html
            if self._is_last():
                pretty_html += '\n' + indent * (self.level - 1)
            html = pretty_html

        return html


class TextNode(Node):
    def __init__(self, document, content, safe=False):
        super().__init__(document)
        self.content = content
        self.safe = safe

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.content)

    def render(self):
        if not self.safe:
            return escape(self.content, quote=False)
        return self.content


class DocumentRoot(XmlNode):
    def __init__(self, document, tag_name, attrs={}):
        self.doc = document
        self.child_nodes = []
        self.parent_node = None
        self.level = 0
        self.tag_name = tag_name
        self.attrs = attrs
        self.content = None
        self.index = 0
        self.safe = False
