#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

from flask import render_template, session
from flask import redirect, url_for
from flask import g, abort, make_response
from flask_login import login_user
from flask_login import logout_user
from flask_login import current_user

from . import main
from .. import db
from ..models import User
from ..api_1_0 import api
from ..models import User
from .. import logger


@main.route('/', methods=['GET'])
def index():
    users = User.query.all()
    users_name = [user.hdoj_username for user in users]
    return render_template('base.html', user=users[0])


@main.route('/profile/<username>')
def profile(username):
    user_name = current_user.hdoj_username
    try:
        user = User.query.get(hdoj_username=users_name)
        return render_template('Homepage.html', user=user)
    except Exception as e:
        logger.info('User <> does not exists'.format(username))
        return abort(make_response('404.html'))
