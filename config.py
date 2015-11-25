# -*- coding:utf-8 -*-
__author__ = 'lulizhou'
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # app路径
    APPDIR = os.path.join(BASEDIR, 'app')
    STATICDIR = os.path.join(APPDIR, 'static')
    UPLOADDIR = os.path.join(STATICDIR, 'uploads')

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
    RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = '1002359548@qq.com'
    FLASKY_POSTS_PER_PAGE = 10
    QINIU_ACCESS_KEY = 'aUHMb5jU2jpgvnTA4HWu8kZehy6i9HFknuwE6XEl'
    QINIU_SECRET_KEY = 'lg_Y4mjgfwKp0HP2YfL-JKe67pJiZv1npo1kCfa3'
    QINIU_BUCKET_NAME = ' picture'
    QINIU_BUCKET_DOMAIN = 'http://7xjj1h.com1.z0.glb.clouddn.com'
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:121224@localhost/blog"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:121224@localhost/blog"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:121224@localhost/blog"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
