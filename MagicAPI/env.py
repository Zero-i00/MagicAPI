import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()


class Environment:
    SECRET_KEY: Final = os.environ.get('DJANGO_SECRET_KEY', '')
    DEBUG: Final = os.environ.get('DEBUG', True)
    SITE_HOST = os.environ.get('SITE_HOST', 'http')
    SITE_IP: Final = os.environ.get('SITE_IP', '0.0.0.0')
    SITE_DOMAIN: Final = os.environ.get('SITE_DOMAIN', '')
    CORS_ORIGIN_ALLOW_ALL: Final = os.environ.get('CORS_ORIGIN_ALLOW_ALL', True)


class PostgresSQL:
    NAME: Final = os.environ.get("POSTGRES_DB")
    USER: Final = os.environ.get("POSTGRES_USER")
    PASSWORD: Final = os.environ.get("POSTGRES_PASSWORD")
    HOST: Final = os.environ.get("POSTGRES_HOST")
    PORT: Final = os.environ.get("POSTGRES_PORT")
