from nose import tools as test
from xmltag.utils import cdata


def test_cdata():
    test.assert_equal(cdata('hello'), '<![CDATA[hello]]>')
