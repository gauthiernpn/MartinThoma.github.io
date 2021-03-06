#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Martin Thoma'
SITENAME = u'Martin Thoma'
SITESUBTITLE = u'A blog about Code, the Web and Cyberculture'
SITEURL = 'https://martin-thoma.de'

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = 'feeds/index.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_USE_SUMMARY = False

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
READERS = {'html': None, 'htm': None}

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'), )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/themoosemind'),
          ('Email', 'mailto:info@martin-thoma.de'),
          ('Github', 'https://github.com/MartinThoma'),
          ('Stackoverflow',
           'http://stackoverflow.com/users/562769/martin-thoma'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './pelican-elegant'
PYGMENTS_STYLE = 'tango'        # Syntax highlighting theme
CUSTOM_CSS = 'static/custom.css'

DISQUS_SITENAME = "martinthoma"


ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

PLUGIN_PATHS = ['./pelican_plugin-render_math',
                './pelican-tipue_search',
                './pelican-toc',
                './pelican-sitemap',
                # './pelican-bootstrapify',
                # './simple_footnotes',
                ]
PLUGINS = ['pelican_plugin-render_math',
           'tipue_search',
           'toc',
           'sitemap',
           'pelican_alias',
           # 'bootstrapify',
           #            'simple_footnotes',
           ]

MD_EXTENSIONS = ["codehilite(css_class=highlight)", "extra", "headerid", "toc",
                 "footnotes"]
MATH_JAX = {'auto_insert': False}

SITEMAP = {
    'exclude': ['tag/', 'category/',
                'tags.html', 'archives.html', 'categories.html'],
    'format': 'xml'
}

TOC = {'TOC_HEADERS': '^h[2-3]',
       'TOC_RUN': 'true'}

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search',
                     '404'))

ARTICLE_EXCLUDES = ['html5', 'js', 'python']
PAGE_EXCLUDES = ['html5', 'js', 'python']

STATIC_PATHS = ['images',
                'extra/CNAME',
                'extra/custom.css',
                'extra/favicon.ico',
                'extra/opensearch.xml',
                'pdf',
                'audio',
                'html5',
                'js',
                'python']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/custom.css': {'path': 'static/custom.css'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/opensearch.xml': {'path': 'opensearch.xml'},
                       'pdf': {'path': 'pdf'},
                       'audio': {'path': 'audio'},
                       'js': {'path': 'js'},
                       'python': {'path': 'python'}}
OUTPUT_PATH = '/var/www/blog/'
# SUMMARY_MAX_LENGTH = 0
