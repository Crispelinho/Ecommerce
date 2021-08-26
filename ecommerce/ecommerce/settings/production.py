from ecommerce.settings.common import *

DEBUG = False
# print(os.environ)
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: update this when you have the production host
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'qualit_ecommerce',       
        # 'USER': 'qualit_ecommerce',  
        # 'PASSWORD': 'QDataSoft2020',  
        # 'HOST': 'localhost', 
        # 'PORT': '3306', 
    }
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
    # print(STATIC_ROOT)
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static','media')
# print(MEDIA_ROOT)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ecommerce/static'),  #Rutas desarrollo
)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "mail.qualityapps.com.co"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="ecommerce@qualityapps.com.co"
EMAIL_HOST_PASSWORD="hV8H9wptEGNRwr5"