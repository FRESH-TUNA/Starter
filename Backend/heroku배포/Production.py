import dj_database_url

DEBUG: TRUE

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'teleguest',
        'USER': 'teleguestRoot',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')



db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)