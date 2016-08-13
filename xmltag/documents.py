from .nodes import XmlNode, TextNode, DocumentRoot
from .renderer import Renderer

doctypes = {
    'xhtml': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">',
    'html4': '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">',
    'html5': '<!DOCTYPE html>',
}


class XMLDocument:
    def __init__(self, root_tag, pretty=True, attrs={}):
        self.current_node = DocumentRoot(self, root_tag, attrs)
        self.indent = '  ' if pretty else None
        self.root_node = self.current_node
        self.renderer = self.get_renderer()

    def get_renderer(self):
        return Renderer(strict_mode=True)

    def __getattr__(self, tag_name):
        def node_wrapper(content=None, _attrs={}, **attrs):
            merged_attrs = dict(_attrs.items() | attrs.items())
            return XmlNode(self, tag_name, attrs=merged_attrs, content=content)
        return node_wrapper

    def render_tag(self, *args, **kwargs):
        return self.renderer.render_tag(*args, **kwargs)

    def render(self):
        return self.root_node.render().strip()

    def text(self, text):
        return TextNode(self, text)


class HTMLDocument(XMLDocument):
    def __init__(self, root_tag='html', doctype='html5', *args, **kwargs):
        super().__init__(root_tag, *args, **kwargs)
        self.doctype = doctypes.get(doctype, doctype) or ''

    def get_renderer(self):
        single_tags = {'meta', 'input', 'img', 'br'}
        return Renderer(strict_mode=False, single_tags=single_tags)

    def render(self):
        html = super().render()
        return self.doctype + (self.indent and '\n' or '') + html


class XHTMLDocument(HTMLDocument):
    def __init__(self, root_tag='html', doctype='xhtml', *args, **kwargs):
        super().__init__(root_tag, *args, **kwargs)
        self.doctype = doctypes.get(doctype, doctype) or ''

    def get_renderer(self):
        single_tags = {'meta', 'input', 'img', 'br'}
        return Renderer(strict_mode=True, single_tags=single_tags)
