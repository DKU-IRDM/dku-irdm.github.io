# site
AUTHOR = "Jinseok Seol"
SITENAME = "IRDM Lab"
SITEURL = "https://dku-irdm.github.io"
SITEDESCRIPTION = "IRDM Lab @ DKU"
THEME = 'theme/'
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'ko'
RECENT_DATA_LIMIT = 5
GOOGLE_ANALYTICS_ID = ''

# urls
RELATIVE_URLS = False

# contents
PATH = 'content/'

# pages
PAGE_PATHS = ['pages/']
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

# articles
ARTICLE_PATHS = [
    'data/headlines/',
    'data/lectures/',
    'data/members/',
    'data/projects/',
    'data/publications/',
]
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
ARTICLE_URL = '{category}/{slug}/'

# statics
STATIC_PATHS = [
    'images/',
    'extra/favicon.ico',
    'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# plugins
PLUGIN_PATHS = ['plugins/']
PLUGINS = [
    'pelican.plugins.sitemap',
    'labsite.engine',
]

# sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'pages': 0.5,
        'articles': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'pages': 'monthly',
        'articles': 'monthly',
        'indexes': 'monthly',
    }
}
