from .nodes import XmlNode, TextNode, DocumentRoot
from .renderer import Renderer

SINGLE_TAGS = {'meta', 'input', 'img', 'br'}
XHTML_DOCTYPE = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
HTML_DOCTYPE = '<!DOCTYPE html>'


class XMLDocument:
    def __init__(self, root_tag, pretty=True, attrs={}):
        self.current_node = DocumentRoot(self, root_tag, attrs)
        self.indent = '  ' if pretty else None
        self.root_node = self.current_node
        self.renderer = Renderer(**self.setup_renderer())

    def setup_renderer(self):
        return dict(strict_mode=True)

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
    def __init__(self, root_tag='html', doctype=HTML_DOCTYPE, *args, **kwargs):
        super().__init__(root_tag, *args, **kwargs)
        self.doctype = doctype or ''

    def setup_renderer(self):
        return dict(strict_mode=False, single_tags=SINGLE_TAGS)

    def render(self):
        html = super().render()
        return self.doctype + (self.indent and '\n' or '') + html


class XHTMLDocument(HTMLDocument):
    def __init__(self, root_tag='html', doctype=XHTML_DOCTYPE, *args, **kwargs):
        super().__init__(root_tag, *args, **kwargs)
        self.doctype = doctype or ''

    def setup_renderer(self):
        return dict(strict_mode=True, single_tags=SINGLE_TAGS)
