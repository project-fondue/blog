#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from datetime import datetime

AUTHOR = u"Project Fondue Team"
SITENAME = u"L'Alpiniste"
SITEURL = 'http://blog.projectfondue.com:9901'
SITESUBTITLE = u"The blog of the Project Fondue Team"

DISQUS_SITENAME = "projectfondue"
TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Blogroll
LINKS = (('Stuart Colville', 'http://muffinresearch.co.uk/'),
          ('Cyril Doussin', 'cyril.doussin.name'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
TAG_CLOUD_STEPS = 10
TAG_CLOUD_MAX_ITEMS = 20

THEME = 'theme'
THEME_STATIC_PATHS = (['static', 'theme/static'])

TWITTER_USERNAME = "projectfondue"
LATEST_POST_LIMIT = 5

YEAR = datetime.now().year

DEFAULT_PAGINATION = 5
RELATIVE_URLS = False

ARTICLE_URL = 'archives/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'archives/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_LANG_URL = 'archives/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = 'archives/{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}.html'

PAGINATION_URL = '{name}-{page_num}'
PAGINATION_SAVE_AS = '{name}-{page_num}.html'

AUTHOR_URL = 'author/{name}'
AUTHOR_SAVE_AS = 'author/{name}.html'

CATEGORY_URL = 'category/{name}'
CATEGORY_SAVE_AS = False
TAG_URL = 'tag/{name}'
TAG_SAVE_AS = 'tag/{name}.html'

# DIRECT TEMPLATES
PAGINATED_DIRECT_TEMPLATES = ('index', 'archives', 'authors', 'author')
DIRECT_TEMPLATES = ('index', 'tags', 'archives')

ARCHIVES_SAVE_AS = 'archives/index.html'
