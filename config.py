# Python
from os import getenv


class Config:
    APP_PORT = getenv('PORT')
    DEBUG = getenv('DEBUG')


class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestingConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

KUBEFLOW_URL = getenv('KUBEFLOW_URL', default="http://ml-pipeline:8888/apis/v1beta1/")
