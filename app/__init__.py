#!/usr/bin/env python
# coding=utf-8

import os
import logging
from datetime import datetime
from flask import Flask, render_template
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config


lm = LoginManager()
# 设置用户登录的安全级别
lm.session_protection='strong'
lm.login_view='main.login'
db = SQLAlchemy()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
logger = logging.getLogger('SutAcm')
file_handler=logging.FileHandler(
                    '../{}.log'.format(datetime.now().strftime("%Y-%m-%d")))
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(name)s- %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


from .models import DBManager
dbm = DBManager()


def create_app(config_name):
    app = Flask(__name__, template_folder='./templates',
                static_folder='./static')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    lm.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    from .auth import auth
    from .api import api
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    return app
