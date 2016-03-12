from tag.nodes import DocumentRoot
from nose import tools as test
from tag.layout import Layout, LayoutError
from unittest.mock import Mock


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


def mock_node():
    node = Mock()
    return node


class MyLayout(Layout):
    render_two_called = False

    def setup_document(self):
        return mock_document()

    def setup_layout(self, doc):
        pass

    def render_one(self, doc):
        pass

    def render_two(self, doc):
        self.render_two_called = True


class TestLayout:
    def setup(self):
        self.layout = MyLayout()

    def test_define(self):
        node = mock_node()
        self.layout.doc.current_node = node

        self.layout.define('one')
        test.assert_equal(self.layout.placeholders['one'], node)

        with test.assert_raises(LayoutError):
            self.layout.define('one')  # already defined

        # cleanup
        self.layout.doc.current_node = self.layout.doc.root_node

    def test_render(self):
        self.layout.render()
        test.assert_false(self.layout.render_two_called)

        self.layout.define('two')
        self.layout.render()
        test.assert_true(self.layout.render_two_called)
