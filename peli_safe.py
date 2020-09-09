#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Brice Loose'
SITENAME = 'Intro to Scientific Computing and Data Analysis (CSC593,OCG404)'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True # false is better for organzing lectures into subfolders

#THEME = 'simplfy-theme'
THEME = './themes/nest'
SITESUBTITLE = u'My Awesome Blog'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages

MENUITEMS = [('Home', '/'),('Assignments','/Assignments')]

STATIC_PATHS = ['static','images']
NEST_HEADER_IMAGES = 'banner.jpg'
#NEST_HEADER_LOGO = 'static/banner.jpg'


# Blogroll
LINKS = None
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = None
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10
DISPLAY_PAGES_ON_MENU = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]

#Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True