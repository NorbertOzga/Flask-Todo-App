import os


def get_database_connection_uri():
    user = os.getenv('POSTGRES_USER', '')
    password = os.getenv('POSTGRES_PASSWORD', '')
    host = os.getenv('POSTGRES_HOST', '')
    database = os.getenv('POSTGRES_DB', '')
    port = os.getenv('POSTGRES_PORT', '')
    return f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_database_connection_uri()


class ProdConfig(Config):
    DEBUG = False
    ENV = 'prod'


class DevConfig(Config):
    DEBUG = True
    ENV = 'prod'
