# _*_ Coding:utf-8 _*_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from config import config


db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    # 注册蓝图
    from app.home import home as home_blueprint
    from app.admin import admin as admin_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint,url_prefix="/admin")

    return app




