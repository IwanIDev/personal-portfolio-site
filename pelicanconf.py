from datetime import datetime
from .markdown import MARKDOWN

AUTHOR = 'Iwan Ingman'
SITENAME = "Iwan's Portfolio"
SITEURL = "http://localhost:8000"

NOW = datetime.now() # Gets the date and time when site is built

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

THEME="themes/PelicanTheme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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


