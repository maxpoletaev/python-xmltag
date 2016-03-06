from nose import tools as test
from tag.utils import cdata


def test_cdata():
    test.assert_equal(cdata('hello'), '<![CDATA[hello]]>')
