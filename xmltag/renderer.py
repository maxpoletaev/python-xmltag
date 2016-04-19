class Renderer:
    def __init__(self, strict_mode=False, single_tags=[]):
        self.single_tags = set(single_tags)
        self.strict_mode = strict_mode

    def render_tag(self, tag, content=None, attrs={}):
        is_single = tag in self.single_tags
        attrs = self.render_attrs(attrs)
        html = '<' + tag

        if attrs:
            html += ' ' + attrs

        html += ' />' if self.strict_mode and (not content and is_single) else '>'

        if content:
            html += content

        if content or not is_single:
            html += '</{}>'.format(tag)

        return html

    def render_attrs(self, attrs):
        result = []
        is_true = set(['true'])
        is_false = set(['false', 'none', 'null'])

        for key, value in attrs.items():
            key = key.strip('_').replace('_', '-')

            if type(value) == bool:
                if value:
                    if self.strict_mode:
                        result.append('{}="{}"'.format(key, key))
                    else:
                        result.append(key)
            else:
                if type(value) != str:
                    value = str(value)
                if value.lower() in is_true:
                    if self.strict_mode:
                        result.append('{}="{}"'.format(key, key))
                    else:
                        result.append(key)
                elif value.lower() not in is_false:
                    result.append('{}="{}"'.format(key, value))

        return ' '.join(result)
