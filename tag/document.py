from .node import XmlNode, TextNode, DocumentRoot


class XmlDocument:
    def __init__(self, root_tag, pretty=True):
        self.current_node = DocumentRoot(self, root_tag)
        self.indent = '  ' if pretty else None
        self.root_node = self.current_node
        self.strict_mode = True

    def __getattr__(self, tag_name):
        def node_wrapper(content=None, **attrs):
            node = XmlNode(self, tag_name, attrs)
            node.content = content
            return node
        return node_wrapper

    def render(self):
        return self.root_node.render()

    def text(self, text):
        return TextNode(self, text)


class HtmlDocument(XmlDocument):
    def __init__(self, root_tag='html', *args, **kwargs):
        super().__init__(root_tag, *args, **kwargs)
        self.doctype = '<!DOCTYPE html>'
        self.strict_mode = False

    def render(self):
        html = super().render()
        return self.doctype + html
