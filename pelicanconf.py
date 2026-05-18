# pelicanconf.py
# Project pelicannew
# Doel is om de werking te doorgronden


from datetime import datetime


AUTHOR = 'Einte Elsinga'
SITENAME = 'Leer pelican en html'
SITEURL = ''
SITETITLE = 'Einte Elsinga'
SITESUBTITLE = 'Leer wat programmeren'
BROWSER_COLOR = '#333333'
PATH = "content"

THEME = 'theme/mijntheme'
# THEMESTATICPATHS = 'theme'
TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MAIN_MENU = True
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

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
MENUITEMS = (
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags')
)

STATIC_PATHS =  ['static' ]
CUSTOM_CSS = 'static/custom.css' # in de document dir
#USE_LESS = True


LINKS = (
    ('Home', '/'),
)

#USE_LESS = True


PLUGIN_PATHS = [
    './pelican-plugins'
]


# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
