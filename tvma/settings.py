import os
import os  # isort:skip
def gettext(s): return s


DATA_DIR = os.path.dirname(os.path.dirname(__file__))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret
SECRET_KEY = '7t!3b3_cih0k#j+uo=-w2rtr1aya9aqqop_bagn0g_iyfngl$7'


DEBUG = True
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', '206.81.10.55']
else:
    ALLOWED_HOSTS = ['206.81.10.55']


# Application definition


ROOT_URLCONF = 'tvma.urls'


WSGI_APPLICATION = 'tvma.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'tvma', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tvma', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',
    'djangocms_file',
    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    'absolute',
    # 'aldryn_forms',
    # 'aldryn_forms.contrib.email_notifications',
    'captcha',
    'emailit',

    'tvma',
]

LANGUAGES = (
    # Customize this
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    # Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    # Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('index-barber.html', 'Barber Theme'),
    ('index-event.html', 'Event Theme'),
    ('b1.html', 'base'),
    ('celebrity.html', 'celebrity')
)

X_FRAME_OPTIONS = 'SAMEORIGIN'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

if DEBUG:
    DATABASES = {
        'default': {
            'CONN_MAX_AGE': 0,
            'ENGINE': 'django.db.backends.sqlite3',
            'HOST': 'localhost',
            'NAME': 'project.db',
            'PASSWORD': '',
            'PORT': '',
            'USER': ''
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bigboy',
            'USER': 'admin_db',
            'PASSWORD': 'focus@1',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
