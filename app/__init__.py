#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


lm = LoginManager()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, template_folder='./templates',
                static_folder='./static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    lm.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
