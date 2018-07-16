#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.first()
    return render_template('base.html', user=user)

