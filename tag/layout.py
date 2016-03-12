class Layout:
    def __init__(self):
        self.placeholders = {}
        self.doc = self.setup_document()
        self.setup_layout(self.doc)

    def setup_document():  # pragma: no cover
        raise NotImplementedError()

    def setup_layout():  # pragma: no cover
        raise NotImplementedError()

    def define(self, place_name, node=None):
        if place_name in self.placeholders:
            raise LayoutError('Placeholder {} already defined.'.format(place_name))
        if not node:
            node = self.doc.current_node
        self.placeholders[place_name] = node

    def render(self):
        for name, node in self.placeholders.items():
            render_method = getattr(self, 'render_' + name, None)
            if render_method:
                self.doc.current_node = node
                render_method(self.doc)
        return self.doc.render()


class LayoutError(Exception):
    pass
