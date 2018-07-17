#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from flask import (render_template, session,
                   redirect, url_for,
                   g)
from flask_login import login_user, logout_user
from . import main
from .. import db
from ..models import User


@main.route('/', methods=['GET'])
def index():
    users = User.query.all()
    users_name = [user.hdoj_username for user in users]
    return render_template('base.html', user=users[0])

