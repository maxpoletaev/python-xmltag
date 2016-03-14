from xmltag import XMLDocument
from datetime import datetime
from collections import namedtuple


def get_posts():
    Post = namedtuple('Post', ['title', 'description'])

    return [
        Post('Post1', 'Description1'),
        Post('Post2', 'Description2'),
    ]


doc = XMLDocument('rss', attrs={
    'xmlns:atom': 'http://www.w3.org/2005/Atom',
    'version': '2.0',
})

with doc.channel():
    doc.title('Hacker News')
    doc.link('https://news.ycombinator.com/')
    doc.description('Links for the intellectually curious, ranked by readers.')
    now = datetime.now().isoformat()
    doc.pubDate(now)

    for post in get_posts():
        with doc.item():
            doc.title(post.title)
            doc.description(post.description)
            doc.pubDate(now)

print(doc.render())
