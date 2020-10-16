class Config:
    pass


class ProdConfig(Config):
    DEBUG = False
    ENV = 'prod'


class DevConfig(Config):
    DEBUG = True
    ENV = 'prod'
