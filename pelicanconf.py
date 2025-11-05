from datetime import datetime

import os
import sys
sys.path.append(os.curdir)

from markdownconf import MARKDOWN


AUTHOR = 'Iwan Ingman'
SITENAME = "Iwan Ingman"
SITEURL = "http://localhost:8000"

NOW = datetime.now() # Gets the date and time when site is built

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME="themes/PelicanTheme"

ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MD_INCLUDE_BASE_PATH = 'pages'
SUMMARY_MAX_LENGTH = 25

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


