===
Tag
===

.. image:: https://travis-ci.org/zenwalker/python-tag.svg?branch=master
    :target: https://travis-ci.org/zenwalker/python-xmltag

.. image:: https://coveralls.io/repos/github/zenwalker/python-tag/badge.svg?branch=master
    :target: https://coveralls.io/github/zenwalker/python-xmltag?branch=master

XMLTag — tool for easy creating XML and HTML documents in the Python style. Idea was taked form yattag_, but *xmltag* offers an improved features with less code (really, api is very small, just see source code).


Installation
============

::

    $ pip install xmltag


Usage example
=============

.. code-block:: python

    from xmltag import HTMLDocument
    doc = HTMLDocument()

    with doc.head():
        doc.title('Document')

    with doc.body():
        doc.h1('Helo world!', class_="heading")
        users = ['Marry', 'John', 'Bob']
        with doc.ul(id='user-list'):
            for name in users:
                doc.li(name)

    print(doc.render())


.. _yattag: http://www.yattag.org/
.. _lxml: http://lxml.de/
