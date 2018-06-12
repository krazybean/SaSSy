class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    DATABASE = 'sassy.db'


class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'
