from ecommerce.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'qualit_ecommerce',       
        # 'USER': 'root',  
        # 'PASSWORD': '',  
        # 'HOST': 'localhost', 
        # 'PORT': '3306', 

    }
}

# print(TEMPLATES)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
if DEBUG:
    STATIC_URL = '/static/static/'
else:
    STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static') # Rutas producción
# print("STATIC_ROOT:",STATIC_ROOT)
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static','media')
# print("BASE_DIR:",BASE_DIR)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'ecommerce/static'),  #Rutas desarrollo
)
# print("STATICFILES_DIRS:",STATICFILES_DIRS)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER="quality.ecommerce2021@gmail.com"
EMAIL_HOST_PASSWORD="e-commerce.2021"