# -*- mode: python; coding: utf-8; -*-
"""
This is your project's main settings file that can be committed to your
repo. If you need to override a setting locally, use local.py
"""

import django
import os, sys
import logging
#import django.conf.global_settings as DEFAULT_SETTINGS
#import memcache_toolbar.panels.memcache

# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")

PYTHON_VERSION = '%s.%s' % sys.version_info[:2]
DJANGO_VERSION = django.get_version()
#path = lambda *a: os.path.join(ROOT, *a)

SUPPORTED_NONLOCALES = ['media', 'admin', 'static']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

#LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'locale'),)
SITE_ID = 1

# Defines the views served for root URLs.
ROOT_URLCONF = 'DjangoApp.urls'

INSTALLED_APPS = [
    'mptt',
    'fiber',
    #'grappelli.dashboard',
    #'grappelli',
    #'grappellifit',
    #'compressor',
    #'filebrowser',

    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    #'modeltranslation_wrapper',
    #'modeltranslation',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',
    'djangorestframework',
    'dajaxice',
    'dajax',
    # Third-party apps, patches, fixes
    ##'commonware.response.cookies',
    'djcelery',
    'gunicorn',
    #'rosetta-grappelli',
    'rosetta',
    #'django_nose',
    #'session_csrf',
    #'debug_toolbar',
    #'debug_toolbar_user_panel',
    #'memcache_toolbar',
    #'easy_thumbnails',
    'widget_tweaks',
    'django_forms_bootstrap',
    'imagestore',
    'sorl.thumbnail',
    'taggit',
    'tagging',
    'photologue',
    'intellipages',
    #'registration',
    'guardian',
    # Database migrations
    'south',
    'knowledge',
    # Application base, containing global templates.
    'DjangoApp.base',
    'userena',
    'userena.contrib.umessages',
    'profiles',

    # Local apps, referenced via DjangoApp.appname
    #'flatpages_plus',
    #'newsly',
    'compressor',
]

# Place bcrypt first in the list, so it will be the default password hashing
# mechanism
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
    )

# Sessions
#
# By default, be at least somewhat secure with our session cookies.
SESSION_COOKIE_HTTPONLY = True

# Set this to true if you are using https
SESSION_COOKIE_SECURE = False

CSRF_COOKIE_IN_EVERY_RESPONSE = True
## Tests
TEST_RUNNER = 'test_utils.runner.RadicalTestSuiteRunner'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.example.com/media/"
MEDIA_ROOT = FILEBROWSER_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.example.com/media/", "http://example.com/media/"
MEDIA_URL = FILEBROWSER_MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public/static')

# URL prefix for static files.
# Example: "http://media.example.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'static',
    )

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
    'compressor.finders.CompressorFinder',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'flatpages_plus.middleware.FlatpageFallbackMiddleware',
    #'commonware.middleware.FrameOptionsHeader',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'userena.middleware.UserenaLocaleMiddleware',
    #'userena.middleware.CsrfFixMiddleware',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    #'session_csrf.context_processor',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.csrf',
    #'jingo_minify.helpers.build_ids',
    "imagestore.context_processors.imagestore_processor",
    )

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
    )

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #'jingo.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
    )

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
    )

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    #('fr', gettext('French')),
    #('es', gettext('Spanish')),
    #('pt', gettext('Portuguese')),
    #('de', gettext('German')),
    ('ru', gettext('Russian')),
    ('ua', gettext('Ukraine')),
    )
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'DjangoApp.translation'
#MODELTRANSLATION_TRANSLATION_FILES = ('DjangoApp',)
# Specify a model to use for user profiles, if desired.
#AUTH_PROFILE_MODULE = 'DjangoApp.accounts.UserProfile'

FILE_UPLOAD_PERMISSIONS = 0664

SOUTH_TESTS_MIGRATE = False

API_RENDER_HTML = True
FIBER_TEMPLATE_CHOICES = (
    ('', 'Default template'),
    ('tpl-home.html', 'Home template'),
    ('tpl-sidebar.html', 'With sidebar template'),
    )
#FIBER_CONTENT_TEMPLATE_CHOICES = (
#    ('', 'Default template'),
#    ('special-content-template.html', 'Special template'),
#)
FIBER_METADATA_CONTENT_SCHEMA = FIBER_METADATA_PAGE_SCHEMA = {
    'title': {
        'widget': 'select',
        'values': ['option1', 'option2', 'option3',],
    },
    'bgcolor': {
        'widget': 'combobox',
        'values': ['#ffffff', '#fff000', '#ff00cc'],
        'prefill_from_db': True,
    },
    'description': {
        'widget': 'textarea',
    },
}

try:
    import seoutils
except ImportError:
    pass
else:
    INSTALLED_APPS = INSTALLED_APPS + ['seoutils']
# Django extensions
try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS = INSTALLED_APPS + ['django_extensions']

if 'fiber' in INSTALLED_APPS:
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
        'fiber.middleware.ObfuscateEmailAddressMiddleware',
        'fiber.middleware.AdminPageMiddleware',
        )
    TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
        'fiber.context_processors.page_info',
        )


# The WSGI Application to use for runserver
WSGI_APPLICATION = 'DjangoApp.wsgi.application'

GRAPPELLI_INDEX_DASHBOARD = 'DjangoApp.dashboard.CustomIndexDashboard'
DIRECTORY = 'uploads/'

# https://github.com/mozilla/django-session-csrf
ANON_ALWAYS = True # always provide CSRF protection for anonymous users (неработает registration Login)

# Add the Guardian and userena authentication backends
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

# Settings used by Userena
LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTH_PROFILE_MODULE = 'profiles.Profile'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_MUGSHOT_SIZE = 140
#USERENA_MUGSHOT_DEFAULT = "http://example.com/gravatar.png"

ACCOUNT_ACTIVATION_DAYS = 2 # кол-во дней для хранения кода активации
DAJAXICE_MEDIA_PREFIX = "dajaxice"
DAJAXICE_DEBUG = True
DAJAXICE_JS_DOCSTRINGS = True
#DAJAX_FUNCTIONS=(
# "userena.ajax.send_form",
# "userena.assign_test",
#)

## Help Desk
KNOWLEDGE_ALLOW_ANONYMOUS = True
KNOWLEDGE_FREE_RESPONSE = False
KNOWLEDGE_SLUG_URLS = False
KNOWLEDGE_ALERTS = True

### imagestore
#IMAGESTORE_LOAD_CSS = False
#IMAGESTORE_SHOW_USER = False
#IMAGESTORE_UPLOAD_TO = 'imagestore/'
IMAGESTORE_TEMPLATE = 'layout_2_col.html'
#IMAGESTORE_SELF_MANAGE = False

## Compress
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc DjangoApp/base/static/less/aplication.less DjangoApp/base/static/css/aplication.css'),
    )

## Rosetta
#ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'

## Log settings

LOG_LEVEL = logging.INFO
LOG_COLORSQL_ENABLE = True
LOG_COLORSQL_VERBOSE = True
#HAS_SYSLOG = True
#SYSLOG_TAG = "http_app_DjangoApp"  # Make this unique to your project.
# Remove this configuration variable to use your custom logging configuration
#LOGGING_CONFIG = None
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'DEBUG',
        'handlers': ['default'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s || %(message)s'
        },
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        'default': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'log/django-app.log',
            'formatter': 'verbose',
        },
        'default-db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log/django-app-db.log',
            'maxBytes': 1024 * 1024 * 5, # 5 MB
            'backupCount': 20,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django': {
            'handlers': ['default'],
            'propagate': False,
            'level': 'DEBUG',
        },
        'dajaxice': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['default-db'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'userena': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG',
        },
        'fiber': {
            'handlers': ['console', 'default'],
            'level': 'DEBUG',
        },
        'DjangoApp': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}
# Needed for Django guardian
ANONYMOUS_USER_ID = -1

try:
    import django_jenkins

    installed_apps = list(INSTALLED_APPS)
    installed_apps.append('django_jenkins')
    INSTALLED_APPS = tuple(installed_apps)
except ImportError:
    pass

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    )

