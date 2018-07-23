#!/usr/bin/env python
# coding=utf-8

from datetime import datetime, timedelta

from flask import jsonify
from flask_login import UserMixin
from flask_login import AnonymousUserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from pymongo import MongoClient

from app import db, lm, logger


FORMATER = '%Y-%m-%d'


class User(db.Model, UserMixin):
    """
    继承UserMixin的
    is_authenticated
    is_active
    is_anonymous
    """

    id = db.Column(db.Integer, primary_key=True)
    hdoj_username = db.Column(db.String(100), nullable=False, unique=True)
    student_id = db.Column(db.String(10), nullable=False, unique=True)
    # 默认算法
    password_hash = db.Column(db.String(128), nullable=False)
    photo_path = db.Column(db.String(100), nullable=False)

    def __init__(self, hdoj_username, student_id, password='00000000'):
        from app.utils.avatar import GenerateImage
        self.hdoj_username = hdoj_username
        self.student_id = student_id
        self.password_hash = generate_password_hash(password)
        GenerateImage(self.student_id).get_image()
        self.photo_path = 'users/{}.png'.format(self.student_id)

    def __str__(self):
        return '<User {}>'.format(self.hdoj_username)

    @property
    def password(self):
        raise AttributeError('Password is not a readbale attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        json_self = {
                'hdoj_username': self.hdoj_username,
                'student_id': self.student_id,
        }
        return jsonify(json_self)


class AnonymousUser(AnonymousUserMixin):
    pass


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class DBManager(object):
    """
    去app.__init__实例化一个对象,
    仅仅提供查询数据
    """

    def __init__(self):
        self.__client = MongoClient('localhost', 27017)
        self.__db = self.__client.SADRA
        self.__collection = self.__db.user

    def find_one(self, user_name):
        try:
            data = self.__collection.find_one({"user": user_name}, {'_id': 0})
            now = datetime.now()+timedelta(days=1)
            days = [(now-timedelta(days=index)).strftime(FORMATER)
                    for index in range(1, 6)]
            result = {}
            for day in days:
                if day not in data['date_ps'].keys():
                    result[day] = []
                else:
                    result[day] = data['date_ps'][day]
            data['date_ps'] = result
            return data
        except Exception as e:
            logger.info("访问的用户不存在")

    def find_one_info(self, username):
        try:
            return self.__collection.find_one({'user': username}, {'_id': 0})
        except Exception as e:
            logger.info('用户不存在')
