===
Tag
===

Tag — tool for easy creating XML and HTML documents in the Python style.

**Note:** Tag is not full featured DOM manipulation library. If you have advanced DOM actions (such as move, clone, etc), use the lxml library.


Example
=======

::

    from tag import HTMLDocument

    doc = HTMLDocument()

    with doc.head():
        with doc.title('Document')

    with doc.body():
        with doc.h1('Helo world!', class_="heading")
        users = ['Marry', 'John', 'Bob']
        with doc.ul(id='user-list'):
            for name in users:
                doc.li(name)

    print(doc.render())
