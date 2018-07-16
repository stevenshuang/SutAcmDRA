#!/usr/bin/env python
# coding=utf-8

import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return {
        'db': db,
        'app': app
    }


@manager.command
def test():
    """测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
