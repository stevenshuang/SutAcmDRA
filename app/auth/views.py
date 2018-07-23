#!/usr/bin/env python
# coding=utf-8

from flask import render_template, request
from flask import redirect, url_for, flash
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from . import auth
from ..models import User
from .. import logger


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_name = request.form.get('username')
        passwd = request.form.get('password')
        try:
            user = User.query.filter_by(hdoj_username=user_name).first()
        except Exception as e:
            logger.info('用户不存在')
        if user is not None and user.verify_password(passwd):
            login_user(user)
            return redirect(
                    request.args.get('next') or
                    url_for('main.index', )
                )
        flash('Invald Username Or Password')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))
