from ecommerce.settings.common import *

DEBUG = True
# print(os.environ)
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
      # 'ENGINE': 'django.db.backends.sqlite3',
      # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'qualit_qadmission',       
        'USER': 'qualit_qdata',  
        'PASSWORD': 'QDataSoft2020',  
        'HOST': 'localhost', 
        'PORT': '3306', 
    }
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=20),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
if DEBUG:
    STATIC_URL = '/static/static/'
else:
    STATIC_URL = '/static/'
    
STATIC_ROOT = os.path.join(BASE_DIR,'static') # Rutas producción

MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static','media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ilm/static'),  #Rutas desarrollo
)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.qualityapps.com.co"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="ecommerce@qualityapps.com.co"
EMAIL_HOST_PASSWORD="hV8H9wptEGNRwr5"