from collections import OrderedDict
from xmltag.renderer import Renderer
from nose import tools as test


class TestRenderer:
    def setup(self):
        single_tags = ['input', 'img']
        self.renderer = Renderer(strict=False, single_tags=single_tags)

    def test_render_tag(self):
        result = self.renderer.render_tag('textarea')
        test.assert_equal(result, '<textarea></textarea>')

        result = self.renderer.render_tag('img')
        test.assert_equal(result, '<img>')

    def test_render_tag_with_content(self):
        result = self.renderer.render_tag('div', content='hello')
        test.assert_equal(result, '<div>hello</div>')

    def test_render_tag_with_attrs(self):
        result = self.renderer.render_tag('div', attrs={'attr': 'value'})
        test.assert_equal(result, '<div attr="value"></div>')

    def test_render_attrs(self):
        result = self.renderer.render_attrs(OrderedDict([
            ('str_attr', 'value'),
            ('bool_attr', True),
            ('str_bool_attr', 'true'),
            ('str_attr2', 'value'),
            ('false_attr', False),
            ('none_attr', None),
        ]))
        test.assert_equal(result, 'str-attr="value" bool-attr str-bool-attr str-attr2="value"')


class TestStrictRenderer:
    def setup(self):
        single_tags = ['input', 'img']
        self.renderer = Renderer(strict=True, single_tags=single_tags)

    def test_render_tag(self):
        result = self.renderer.render_tag('textarea')
        test.assert_equal(result, '<textarea></textarea>')

        result = self.renderer.render_tag('img')
        test.assert_equal(result, '<img />')

    def test_render_tag_with_content(self):
        result = self.renderer.render_tag('div', content='hello')
        test.assert_equal(result, '<div>hello</div>')

    def test_render_tag_with_attrs(self):
        result = self.renderer.render_tag('div', attrs={'attr': 'value'})
        test.assert_equal(result, '<div attr="value"></div>')

    def test_render_attrs(self):
        result = self.renderer.render_attrs(OrderedDict([
            ('str_attr', 'value'),
            ('bool_attr', True),
            ('str-bool-attr', 'true'),
            ('str_attr2', 'value'),
            ('false_attr', False),
            ('none_attr', None),
        ]))
        test.assert_equal(result, (
            'str-attr="value" bool-attr="bool-attr" ' +
            'str-bool-attr="str-bool-attr" str-attr2="value"'
        ))
