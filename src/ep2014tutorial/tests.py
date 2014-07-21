import os
import unittest
from webtest import TestApp
from pyramid import paster

here = os.path.dirname(__file__)
test_dir = os.path.join(here, 'testing')
conf = os.path.join(test_dir, 'testing.ini')

default_app = None
def get_app():
    global default_app, app
    if default_app is None:
        default_app = paster.get_app(conf, 'main')
    app = default_app
    return app

def setUp(test, app_func=get_app):
    app = app_func()
    testapp = TestApp(app)
    test.globs['browser'] = testapp

