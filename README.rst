===
Tag
===


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
