#!/usr/bin/env python
# coding=utf-8

from flask import jsonify
from flask_login import login_required
from . import api
from ..models import User
from .. import dbm


@api.route('/users')
def get_user_data():
    users = User.query.all()
    users_name = [user.hdoj_username for user in users]
    user_list = []
    for user_name in users_name:
        user_list.append(dbm.find_one(user_name))
    return jsonify({'users': user_list})
