import      configparser

from        .base               import *





DEBUG = True


INSTALLED_APPS += [
    'debug_toolbar',

]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]





CONFIG_DIR = os.path.join(BASE_DIR, 'config/')

parser = configparser.ConfigParser()
parser.read_file(open(os.path.join(CONFIG_DIR, 'app.ini')))

DATABASES = {}


#Done with postgresql 
DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
        'NAME'      : parser.get('Ruthrestaurant', 'name'),
        'USER'      : parser.get('Ruthrestaurant', 'user'),
        'PASSWORD'  : parser.get('Ruthrestaurant', 'password'),
        'HOST'      : parser.get('Ruthrestaurant', 'host') or '127.0.0.1',
        'PORT'      : parser.getint('Ruthrestaurant', 'port') or '5432',

    }
}



# Tried with Sqlite3 database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



#DEBUG TOOLBAR SETTINGS
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS'   : False,
    'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
}



ENVIRONMENT = 'DEVELOPMENT'

print("\n")
print("DEBUG        = ", DEBUG)
print("MODE         = ", ENVIRONMENT)
print("TEMPLATES    = ", TEMPLATES[0]['DIRS'])
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT)
print("\n")
