#!/usr/bin/env python
# coding=utf-8


from flask_httpauth import HTTPBasicAuth
from flask import g
from ..models import User
auth = HTTPBasicAuth()


@auth.verify_password()
def verify_password(hdoj_username, password):
    if hdoj_username == "":
        g.current_user = AnonymousUser()
        return True
    user = User.query.filter_by(hdoj_username=hdoj_username).first()
    g.current_user = user
    return user.verify_password(password)
