from unittest.mock import Mock
from nose import tools as test
from tag.documents import (
    XMLDocument, HTMLDocument, XHTMLDocument,
    HTML_DOCTYPE, XHTML_DOCTYPE,
)


def mock_renderer():
    renderer = Mock()

    def render_tag(tag, content, *args, **kwargs):
        return '<{t}>{c}</{t}>'.format(t=tag, c=content)
    renderer.render_tag = render_tag


class TestXMLDocument:
    def setup(self):
        self.doc = XMLDocument(root_tag='xml')
        self.renderer = mock_renderer()

    def test_tag(self):
        test.assert_equal(repr(self.doc.html()), 'XmlNode(html)')
        test.assert_equal(repr(self.doc.text('hello')), 'TextNode(hello)')

    def test_render_tag(self):
        result = self.doc.render_tag('html')
        test.assert_equal(result, '<html></html>')

    def test_render(self):
        test.assert_equal(self.doc.render(), '<xml></xml>')


class TestHTMLDocument:
    def setup(self):
        self.doc = HTMLDocument()

    def test_render(self):
        test.assert_equal(self.doc.render(), '{}\n<html></html>'.format(HTML_DOCTYPE))


class TestXHTMLDocument:
    def setup(self):
        self.doc = XHTMLDocument()

    def test_render(self):
        test.assert_equal(self.doc.render(), '{}\n<html></html>'.format(XHTML_DOCTYPE))
