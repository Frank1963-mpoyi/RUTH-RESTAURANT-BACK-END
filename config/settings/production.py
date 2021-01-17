import      dj_database_url
from        decouple            import          config
from        .base               import *



DEBUG               = config('DEBUG')

ALLOWED_HOSTS       = ['*']



MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



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




BASE_PATH       = os.path.join(BASE_DIR)
APP_STATIC      = 'transport/static/'

STATIC_URL      = '/static/'
STATIC_ROOT     = os.path.join(BASE_PATH, APP_STATIC)


MEDIA_URL       = '/media/'
MEDIA_ROOT      = os.path.join(BASE_PATH, f'{APP_STATIC}/media')




# Honor the 'X-Forwarded-Proto' header fro request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



STATICFILES_STORAGE     = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



#DATABASES['default'] =  dj_database_url.config()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':     config('DB_NAME'),
        'USER':     config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST':     config('DB_HOST'),
        'PORT':      config('DB_PORT') 
    }

}

prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)

ENVIRONMENT = 'PRODUCTION'

print("\n")
print("DEBUG        = ", DEBUG      )
print("MODE         = ", ENVIRONMENT)
print("STATIC_ROOT  = ", STATIC_ROOT)
print("MEDIA_ROOT   = ", MEDIA_ROOT )
print("\n")

# Note : dont forget to include production in wsgi