#!/usr/bin/env python
# coding=utf-8

from flask import render_template
from flask_login import login_required

from . import main


@main.route('/', methods=['GET'])
def index():
    return render_template('base.html')


@main.route('/homepage')
@login_required
def profile():
    # ajax去请求数据
    return render_template('Homepage.html')
