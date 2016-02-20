from tag.renderer import Renderer
from nose import tools as test


class TestRenderer:
    def setup(self):
        single_tags = {'input', 'img'}
        self.renderer = Renderer(strict=False, single_tags=single_tags)

    def test_render_tag(self):
        result = self.renderer.render_tag('textarea')
        test.assert_equal(result, '<textarea></textarea>')
