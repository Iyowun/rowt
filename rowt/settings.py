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
ROWT_REDIRECT_URL = "https://rowt.co.uk/thanks"
ROWT_ESTIMATED_CRAWL = 85
ROWT_ESTIMATED_VISIT = 5000
ROWT_ESTIMATED_CONVERSIONS = 2.5

MAILERSEND_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOGVhN2RlNThhMDVmYTA1MDgyMGQwNjRlYjViNmVkNTExYzZlYTMyNTgyYjUxNWNlMmJhOTk3YTk2OThlZDcwNTllNWE0MWY2ODZlMDUwNDgiLCJpYXQiOjE2NTIzNTkxNjMuMTM0MjI5LCJuYmYiOjE2NTIzNTkxNjMuMTM0MjMyLCJleHAiOjQ4MDgwMzI3NjMuMTI5NjY3LCJzdWIiOiIyNjgxMCIsInNjb3BlcyI6WyJlbWFpbF9mdWxsIiwiZG9tYWluc19mdWxsIiwiYWN0aXZpdHlfZnVsbCIsImFuYWx5dGljc19mdWxsIiwidG9rZW5zX2Z1bGwiLCJ3ZWJob29rc19mdWxsIiwidGVtcGxhdGVzX2Z1bGwiLCJzdXBwcmVzc2lvbnNfZnVsbCIsInNtc19mdWxsIl19.Ohq2K1f3ijoCK5eh210hYnh9mgA9zKN1weZWHVLUGBF9U5JHkZPkPGHwE2jj1zGA2aLK1up_7fa54dL0W3yCTCTwPGunGGG2JvfAREoE9dyE3vCcsWQ8IHrl3MRRhU8VzCIUuRBjNyfUGGUdDs5BZTQ5hmSsejpbW7n-t8yYysx1ZxYXO7FINbzSFyOPNGvzZmwkrolyDJMNZ_iWwjzR94-RpPX3MlIkImMEV_2aWgSD2L291-w17CqoANNthnz5IKbjeDgMEJVx0i1XWtFC-s13awyadfv3Ecl236ZryNZzH4SZw70QY5hbVuGCWtP18uCL3n4h0da46BsudTyKerM5KGUjizbRq90C9TwGGoLdj01dbTHboR22OBPIPgQSVfvZbz2O0s5REJHysie9e2Hof1mP_kJ7fnyICzVP70Euxus131a1a9bAYrnNC3CLoPsrAu4vFfoUqIDvGDogvUpSk2WVuq-0k0ZW0HEoN-R1MIxJEqsbI44akDiWWOyHkbPpnSr6KONbCaQkSuxun92Oey2ZZjogHdF7iT7b147AZ6I_TRHlmuKVtiSH_3UF7PD9tj22sHtofX5UmIwGRc9E5iaiYdB4y3WDRgyj5kR5cURBzacYTNSYddfmjhfEOh9v2PsmEufRS5EQQ3uwqVQML6RhUUPq98JoA17JLXI"
MAILERLITE_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiYWVjODQ2OTgwZjY3NjZkMTllYWRjMmUxNTM5ODlkY2ZjOWE2MzdhYjhmNjRjYWU1MGE0MDA3MTJiMzBmZjA1YzQ0MzdiZTQ2YTVmMTRkMDIiLCJpYXQiOjE2NTIzNTczODkuNjM3MzUyLCJuYmYiOjE2NTIzNTczODkuNjM3MzU1LCJleHAiOjQ4MDgwMzA5ODkuNjMwOTYyLCJzdWIiOiI2NjIyMyIsInNjb3BlcyI6W119.uFb1LvkJfsTtW_DQtvhR0nvDGNJDrYdNCp74VWydE74QgRUdBhz1G0aKX1HiKtVeDvB3XDix-2MDzdNlx4Diwxk5c9Yq6xioyjG5G9vKEFIWTipQiJwrXdIYe-B7Lyp3DEOUlUmoIMcSGEJfs9CgllsxeF5l4Vp7ZUNt0M-G7yCQMQQnuYCkKtE4AKafdjprtk3VsRCrbyaX1igbgBJFtE8aKrGRNxEOHsLZZOs5CgikMMNlRDJTLw30W3ptxlMFBEfdnGzuSpDzHSrife5YxmkJc3VzaeYxrx8FXt6KqoBFfUIRkCFpr2Mot7v_FNDagVOtoi0rKAPDDqPs_8mDNfWJlc0f8p56iWOrHR7r2aIuN2MkLVC2Y1-R834r7NCQcU6lyRlcFhWE4r-FkUHFMXO_Gr2VVidcelnGVgqszPKDS1GjhuQtZsGK_40hgqj2d9NBJoD3ecI6lfuv1LGJmdKYHTRT1VNhLIX3Q_aLqRQYDG5YVu6azu89OUUj-nD2mUgGTONAy4Z34etO5U_fC1ir7Im9gtRXTghFqcOQrvBdHa2zxiv7QtVWPlfcP0MTqLTH03TS5bE3AN1v3SJOifXTWNvMyGNsPwdvc925q2ecQN1PwgKx6raw8an5BDwW-skA_OJp8U04OLFP8RpPrGG82f3z3OjoIzOcKIeSQms"