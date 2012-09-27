# -*- mode: python; coding: utf-8; -*-
"""
This is your project's main settings file that can be committed to your
repo. If you need to override a setting locally, use local.py
"""

import os
import logging
#import memcache_toolbar.panels.memcache

# Your project root
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__) + "../../../")
#path = lambda *a: os.path.join(ROOT, *a)
# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'base_css': (
            'css/style.css',
        ),
    },
    'js': {
        'libs_js': (
            'js/libs/jquery-1.6.2.min.js',
            'js/libs/modernizr-2.0.6.min.js',
        ),
    }
}

SUPPORTED_NONLOCALES = ['media', 'admin', 'static']

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

#LOCALE_PATHS
SITE_ID = 1

# Defines the views served for root URLs.
ROOT_URLCONF = 'kvazar.urls'

INSTALLED_APPS = [
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    # Template apps
    'jingo_minify',

    # Django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.syndication',
    'django.contrib.staticfiles',

    # Third-party apps, patches, fixes
    'commonware.response.cookies',
    'djcelery',
    #'django_nose',
    'session_csrf',
    #'debug_toolbar',
    #'debug_toolbar_user_panel',
    #'memcache_toolbar',
    'widget_tweaks',
    'taggit',
    'intellipages',
    'django_extensions',
    'registration',
    # Database migrations
    'south',

    # Application base, containing global templates.
    'kvazar.base',

    # Local apps, referenced via kvazar.appname
    'flatpages_plus',
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
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_csrf.CsrfMiddleware',  # Must be after auth middleware.
    #django.middleware.csrf.CsrfViewMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',
    'flatpages_plus.middleware.FlatpageFallbackMiddleware',
    #'commonware.middleware.FrameOptionsHeader',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'session_csrf.context_processor',
    'django.contrib.messages.context_processors.messages',
    #'jingo_minify.helpers.build_ids',
]

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
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
)

gettext = lambda s: s

LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('es', gettext('Spanish')),
    ('pt', gettext('Portuguese')),
    ('de', gettext('German')),
    ('ru', gettext('Russian')),
)
# Specify a model to use for user profiles, if desired.
#AUTH_PROFILE_MODULE = 'kvazar.accounts.UserProfile'

FILE_UPLOAD_PERMISSIONS = 0664

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
    'kvazar',
    'registration',
    'debug_toolbar',
    'debug_toolbar_user_panel',
    'memcache_toolbar',
]

#JINJA_CONFIG = {'extensions': ['jinja2.ext.i18n', 'jinja2.ext.InternationalizationExtension'],}
# The WSGI Application to use for runserver
WSGI_APPLICATION = 'kvazar.wsgi.application'

GRAPPELLI_INDEX_DASHBOARD = 'kvazar.dashboard.CustomIndexDashboard'
DIRECTORY = 'uploads/'

# https://github.com/mozilla/django-session-csrf
ANON_ALWAYS = True # always provide CSRF protection for anonymous users (неработает registration Login)

ACCOUNT_ACTIVATION_DAYS = 2 # кол-во дней для хранения кода активации

## Log settings

LOG_LEVEL = logging.INFO
HAS_SYSLOG = True
SYSLOG_TAG = "http_app_kvazar"  # Make this unique to your project.
# Remove this configuration variable to use your custom logging configuration
LOGGING_CONFIG = None
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'kvazar': {
            'level': "DEBUG"
        }
    }
}
