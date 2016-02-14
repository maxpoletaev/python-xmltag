def render_tag(tag, content=None, _single=False, _strict=False, attrs={}):
    attrs = render_attrs(attrs, _strict=_strict)
    html = '<' + tag

    if attrs:
        html += ' ' + attrs

    html += ' />' if _strict and (not content or not _single) else '>'

    if content:
        html += content

    if content or not _single:
        html += '</%s>' % tag

    return html


def render_attrs(attrs, _strict=False, exclude=[]):
    result = []
    is_true = ['true']
    is_false = ['false', 'none', 'null']

    for key, value in attrs.items():
        if key.startswith('_'):
            key = key[1:]

        key = key.strip('_').replace('_', '-')

        if type(value) == bool:
            if value:
                if _strict:
                    result.append('%s="%s"' % (key, key))
                else:
                    result.append(key)
        else:
            if type(value) != str:
                value = str(value)

            if value.lower() in is_true:
                if _strict:
                    result.append('%s="%s"' % (key, key))
                else:
                    result.append(key)

            if value.lower() not in is_false:
                result.append('%s="%s"' % (key, value))

    return ' '.join(result)
