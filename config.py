# -*- coding=utf-8 -*-
import os


class Config:
    SECRET_KEY = os.urandom(24)
    # 开启数据库自动跟踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 发送邮件配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = True
    # MAIL_USE_SSL
    MAIL_USERNAME = 'hijack@qq.com'
    MAIL_PASSWORD = 'fqysomnrtndrbfej'
    MAIL_DEFAULT_SENDER = 'hijack@qq.com'

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass


# the config for development
class DevelopmentConfig(Config):
    """数据库配置"""
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xlc123@127.0.0.1:3306/shop'
    DEBUG = True


# define the config
config = {
    'default': DevelopmentConfig
}
