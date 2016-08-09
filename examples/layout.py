from xmltag import Layout, HTMLDocument


class PageLayout(Layout):
    def setup_document(self):
        return HTMLDocument()

    def setup_layout(self, doc):
        with doc.head():
            with doc.title():
                self.define('title')
        with doc.body():
            with doc.header():
                self.define('header')
            with doc.nav(class_='menu'):
                self.define('menu')


class Page(PageLayout):
    def render_title(self, doc):
        doc.text('Hello world')

    def render_header(self, doc):
        doc.h1('Hello, World!')

    def render_menu(self, doc):
        with doc.ul():
            with doc.li(class_='active'):
                doc.a('Home', href='/')
            with doc.li():
                doc.a('Blog', href='/blog')
            with doc.li():
                doc.a('About', href='/about')


print(Page().render())
