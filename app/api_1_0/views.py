#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from flask import jsonify
from flask_login import current_user
from . import api
from ..models import User
from .. import dbm


@api.route('/users')
def get_user_data():
    # 不传一拖过去, 在服务端处理好, 不要在前端处理
    # 用户按做题数排名,
    users = User.query.all()
    users_name = [user.hdoj_username for user in users]
    user_list = []
    for user_name in users_name:
        user_list.append(dbm.find_one(user_name))    # 只拿五条数据
    user_list = sorted(user_list, key=lambda x: x['count'], reverse=True)
    return jsonify({'users': user_list})


@api.route('/user')
def user_detail():
    """通过api抓取用户的主要信息, ajax在打开页面的时候直接请求"""
    user_name = current_user.hdoj_username
    user = User.query.filter_by(hdoj_username=user_name).first()
    user_info = dbm.find_one_info(user_name)
    return jsonify({'date': datetime.now(),
                    'photo_path': user.photo_path,
                    'user_info': user_info})
