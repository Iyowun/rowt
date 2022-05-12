from pathlib import Path
import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qs@!3ee%+9!o)m!7yavxu%o$*&s!hm9uh1r-_$44p9yfbo5hj='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['rowt.co.uk','localhost','127.0.0.1','seal-app-tamk6.ondigitalocean.app']


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rowt',
    'app',
    'form',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rowt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rowt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# constants for rowt calculations
ROWT_REDIRECT_URL = "https://relcanonical.com/account/request"
ROWT_ESTIMATED_CRAWL = 85
ROWT_ESTIMATED_VISIT = 5000
ROWT_ESTIMATED_CONVERSIONS = 2.5

MAILERSEND_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNjljMThhNWVmNjJhODBiNmUwNWMzZDY3ODI3ZDViMGRhZDA1MmE2YjRmNTFkOWNhNjllNTRiY2Y4NDcxMTgzYTE0NjIyMTVhODZiYmZmYzEiLCJpYXQiOjE2NTIyNDY1ODMuMTYxODY4LCJuYmYiOjE2NTIyNDY1ODMuMTYxODcxLCJleHAiOjQ4MDc5MjAxODMuMTU3OTc4LCJzdWIiOiIyNjQ4MyIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCIsInNtc19mdWxsIl19.e601MvEEKkk8504z2qzidjvjv_OqiaYnWxs6kZqk-cidpD8788JWReVXnokqduW6W8rB_C9Zxrzqn3xdyxkaN0g6J3btSUYKBqQQGiZQG7XXPMMDeK5JdLzUK8kxFo39v138b4-zfng--Ne8njDvKBvQYoYtD40mOO-sa_iy6E7Fa_fqyjvQ2BLZBxMoQoMWz4V7xbwTdDwvoH3rdAvX1K_RHi6YPQB3gESoiWg9YB3Toz3nF75D_mVQUoINS0IBpG0e7Cx57W4qqaMs7_S3Z2cklEUjNp3LRi0tQn1lkBsK-t576995SMWQH0GabEckXE9k8_-1wAv33zNF6aRQWj5u7wxFMmShI_IE1VAnd078dnTDqqkVoIPCm5qX0naGNUkejdpngSg6hMQn6xD9kiv7o0Hff0klk36ukuwHVvXBTbPm2CIQ2leCBgjr5rvJpm-aJEINu43dqolOT9aLwxtmwvaTli7Zaaf3YvCX1Bh5Nbw0azY3OV2GqwG_I1GgTJO0O0syrWjhP4rD2fK2WL98MKGBNgmhLY-bmyIumqO1086wY4tx2ktDP-DvjajQtBrCJx_6HzfRo8v5p1mFkfuGG80FudZrUjIxw0hf5JacZkNfLot-plLTHjk-jztYPR_lDzVDQGTlLGXT_Y6OWP2ZPQmKurzFghrQNI_4ARs"
MAILERLITE_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiOWI0NTQyNGVmYjUwYTUxYzQ1ZjZlZDZmYThkYjNmNDlhZDhmOGU3MGQ2MTM4NzhjZmU3NjA4MTA0YjM4ZWUwOGJhYzU4OWE5ZTRkNzAyMWQiLCJpYXQiOjE2NTIyNDY2MTcuNDg1MzI0LCJuYmYiOjE2NTIyNDY2MTcuNDg1MzI5LCJleHAiOjQ4MDc5MjAyMTcuNDc5Njc3LCJzdWIiOiI2MTQ0MCIsInNjb3BlcyI6W119.fOJKZpipxipTh9iC1Fmw-yx6Tw_ix3mttA_NvYWFQoG-H_VCEJxHSK9Zp2sb7TkVmBa-V0ffrjBm720EIbYYF753s3v5IGy4QSFHJRuQKNwpKAEFFwL8e-hwoGA0tWPf-zD8yXFQxTMqUQJrt8wr_XQto-WvzAHEgHR5F4jgjZ7nKVbzEktEuASV3yoooFOapxBdONGKnh-VPTmq9Ypi4i3yOg-Uv5dA0SVkfHUCFX_4lv-Hp4pzPTOCnRQ0RY0OQePc8yWO4v2Anb62lxshkD75PbrV4hNEL0i-VB0ADeThmZaSH2KuvRVep0OHfAsejdhuWUOs5vzGaq_phi6yojTOqXfdsA-56HJhlFnJ2qwFx1C_KdzwMw0K7lORzwWnOVl-qZClLTOBfQqi-QeTlLBOfVSiXxU1UJEp1HzkcUIp1SknV4XVbegERpnQCzNMKFBLfScm3aH8oRzcKRfoBvBQD18XhkpQz9zlCWliKVbl6CTWdNPZXa9dxalhXWehONiIMrnSZaVbxcj4KMjizU0ONV1qjnrJ_62qzsd85QqLD-GhQonkatU7LcPDOjX8-kG1gQxe7Ehd_YhMlhGQ-pSmEdfv227MN9rzpEtGPD450TWWhFW8cPaPXUdHbIsqPRSu3Uu4HHzvxISH84t8ZuNdQmj4kzb0X_IA8-3TFLI"