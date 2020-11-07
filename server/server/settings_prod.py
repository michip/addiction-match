from .settings import *

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql_psycopg2"),
        "NAME": os.environ.get("SQL_DATABASE", "junction"),
        "USER": os.environ.get("SQL_USER", "junction"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "junction"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

DEBUG = True
