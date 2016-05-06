======
XMLTag
======

.. image::
    https://img.shields.io/pypi/v/xmltag.svg
    :target: https://pypi.python.org/pypi/xmltag

.. image::
    https://travis-ci.org/zenwalker/python-xmltag.svg
    :target: https://travis-ci.org/zenwalker/python-xmltag

.. image::
    https://coveralls.io/repos/github/zenwalker/python-xmltag/badge.svg
    :target: https://coveralls.io/github/zenwalker/python-xmltag

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

More examples are in examples_ directory.


Layouts
=======

You can create layouts for reusing code.

.. code-block:: python

    class PageLayout(Layout):
        def setup_document(self):
            return HTMLDocument()

        def setup_layout(self, doc):
            with doc.head():
                with doc.title():
                    self.define('title')

1. Define ``setup_document`` method and return document instance from it.
2. Write layout in ``setup_layout`` method and define placeholders using ``self.define`` method.

Following this actions you can inherit from ``PageLayout`` and define ``render_title`` method.

.. code-block:: python

    class Page(PageLayout):
        def render_title(self, doc):
            doc.text('Hello World!')


Escaping
========

XMLTag does not provide escaping content by default.
You should manualy escape unsafe content for example using ``html.escape``.

.. code-block:: python
    import xmltag
    import html

    with doc.div(class_='user-comment'):
        doc.text(html.escape(unescaped_text))


.. _yattag: http://www.yattag.org/
.. _examples: https://github.com/zenwalker/python-xmltag/tree/master/examples
