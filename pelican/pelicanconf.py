#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'dictoss@live.jp'
SITENAME = 'Cross Distro Developers Camp'
SITEURL = 'https://dictoss.github.io/xddc'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DATE_FORMATS = {
    'ja': '%Y-%m-%d',
    'en': '%Y-%m-%d',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>).*'

"""
theme blue-penguin custimize option
"""
THEME = './blue-penguin'

# all the following settings are *optional*

# HTML metadata
SITEDESCRIPTION = 'Cross Distro Developers Camp'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

#
ARTICLE_URL = '{slug}.html'

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL           = 'tags'
TAGS_SAVE_AS       = 'tags.html'
AUTHORS_URL        = 'authors'
AUTHORS_SAVE_AS    = 'authors.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    #('Tags', TAGS_URL, TAGS_SAVE_AS),
    ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
MENUITEMS = (
    #('GitHub', 'https://github.com/'),
    #('Linux Kernel', 'https://www.kernel.org/'),
)
