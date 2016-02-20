from tag.nodes import Node, XmlNode, TextNode, DocumentRoot
from unittest.mock import Mock
from nose import tools as test


def mock_document():
    doc = Mock()
    root = DocumentRoot(doc, 'html')
    doc.current_node = root
    doc.root_node = root

    def render_tag(tag, content, *args, **kwargs):
        return '<{t}>{c}</{t}>'.format(t=tag, c=content)

    doc.render_tag = render_tag
    doc.indent = None
    return doc


class TestNode:
    def test_with(self):
        doc = mock_document()
        with Node(doc) as html_node:
            test.assert_equal(doc.current_node, html_node)
        test.assert_equal(doc.current_node, doc.root_node)

    def test_append_to(self):
        doc = mock_document()
        root = XmlNode(doc, 'html')
        child = XmlNode(doc, 'body')
        child.append_to(root)
        test.assert_equal(root.child_nodes, [child])

    def test_is_last(self):
        doc = mock_document()
        root = XmlNode(doc, 'html')
        child_one = XmlNode(doc, 'head').append_to(root)
        child_two = XmlNode(doc, 'body').append_to(root)
        test.assert_false(child_one._is_last())
        test.assert_true(child_two._is_last())


class TestXmlNode:
    def test_init(self):
        doc = mock_document()
        node = XmlNode(doc, 'html', attrs={'lang': 'en'})
        test.assert_equal(node.tag_name, 'html')
        test.assert_equal(node.attrs, {'lang': 'en'})

    def test_repr(self):
        node = XmlNode(mock_document(), 'html', attrs={'lang': 'ru'})
        test.assert_equal(repr(node), 'XmlNode(html, lang=ru)')

    def test_render(self):
        doc = mock_document()
        node = XmlNode(doc, 'html', attrs={'lang': 'en'})
        body = XmlNode(doc, 'body', content='hello world')
        node.child_nodes.append(body)
        test.assert_equal(node.render(), '<html><body>hello world</body></html>')

    def _test_render_pretty(self):
        doc = mock_document()
        doc.indent = '..'
        node = XmlNode(doc, 'html')
        node.child_nodes.append(XmlNode(doc, 'body'))
        test.assert_equal(node.render(), '<html>\n..<body></body>\n</html>')


class TestTextNode:
    def setup(self):
        self.doc = mock_document()

    def test_render(self):
        node = TextNode(self.doc, 'hello world')
        test.assert_equal(node.render(), 'hello world')

    def test_repr(self):
        node = TextNode(self.doc, 'hello world')
        test.assert_equal(repr(node), 'TextNode(hello world)')
