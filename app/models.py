#!/usr/bin/env python
# coding=utf-8

from hashlib import md5
from flask import jsonify

from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    hdoj_username = db.Column(db.String(100), nullable=False, unique=True)
    student_id = db.Column(db.String(10), nullable=False, unique=True)
    # 默认算法
    password = db.Column(db.String(128), nullable=False)
    photo_path = db.Column(db.String(100), nullable=False)


    def __init__(self, hdoj_username, student_id, password='00000000'):
        from app.utils.avatar import GenerateImage
        self.hdoj_username = hdoj_username
        self.student_id = student_id
        self.password = md5(password.encode('utf-8')).hexdigest()
        GenerateImage(self.student_id).get_image()
        self.photo_path = 'users/{}.png'.format(self.student_id)

    def to_json(self):
        json_self = {
                'hdoj_username': self.hdoj_username,
                'student_id': self.student_id,
        }
        return jsonify(json_self)
