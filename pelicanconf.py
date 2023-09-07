#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brice Loose'
SITENAME = u'2021 | Data Prototyping and Scientific Computing'
SUBTITLE = 'Fall 2021'
SITEURL = 'https://bloose.github.io/data_prototyping_scientific_computing'

RELATIVE_URLS = True
PATH = 'content'

TIMEZONE = 'America/New_York'

USE_FOLDER_AS_CATEGORY = False # false is better for organzing lectures into subfolders
PYGMENTS_STYLE = 'colorful'  # without this it was using black background and light font
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#USE_FOLDER_AS_CATEGORY = True # false is better for organzing lectures into subfolders
Links = None

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
#DISPLAY_TAGS_ON_SIDEBAR=True
#DISPLAY_RECENT_POSTS_ON_SIDEBAR=True
#RECENT_POST_COUNT=10

# Social widget
SOCIAL = None

DEFAULT_PAGINATION = False


I18N_TEMPLATES_LANG = 'en'


THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'lumen'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['./plugins','./pelican-plugins']
MARKUP = ('md', 'ipynb')
PLUGINS = ['i18n_subsites','ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]


MENUITEMS = [('Syllabus', 'pages/OCG404_CSC593_Syllabus_2021.pdf')]

STATIC_PATHS = ['Assignments','images']

CUSTOM_CSS = 'static/css/custom.css'
CUSTOM_JS = 'static/js/custom.js'

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}


NEST_HEADER_IMAGES = 'banner.jpg'
#NEST_HEADER_LOGO = 'static/banner.jpg'
BANNER = 'images/banner2.jpg'

IPYNB_COLORSCHEME = 'colorful'
