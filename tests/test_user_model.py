#!/usr/bin/env python
# coding=utf-8

import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):

    def test_password_setter(self):
        u = User('test_user', '1555555', '1234556')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User('test_user', '155555', '1234556')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verify(self):
        u = User('test_user', '1555555', '123456')
        self.assertTrue(u.verify_password('123456'))
        self.assertFalse(u.verify_password('1223'))
