#!/usr/bin/env python
# coding=utf-8

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = 'Coco'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <xxxxx@gmail.com>'
    FLASKY_ADMIN = 'Coco'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'xxxxx@gmail.com'
    MAIl_PASSWORD = '123456'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pwd@localhost:3306/SRDRA'


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pwd@localhost:3306/SRDRA'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:pwd@localhost:3306/SRDRA'


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
