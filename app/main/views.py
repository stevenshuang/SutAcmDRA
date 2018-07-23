#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

from flask import render_template, session
from flask import redirect, url_for
from flask import g, abort, make_response
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user
from flask_login import login_required

from . import main
from .. import db
from ..models import User
from ..api_1_0 import api
from ..models import User
from .. import logger


@main.route('/', methods=['GET'])
def index():

    return render_template('base.html')


@main.route('/homepage')
@login_required
def profile():
    # ajax去请求数据
    return render_template('Homepage.html')
