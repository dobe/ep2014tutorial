import os
import unittest
import doctest
from pprint import pprint
from webtest import TestApp
from pyramid import paster
from . import testing
from . import model

here = os.path.dirname(__file__)
test_dir = os.path.join(here, 'testing')
conf = os.path.join(test_dir, 'testing.ini')

schema_sql = os.path.join(here, 'schema.sql')

default_app = None


def get_app():
    global default_app, app
    if default_app is None:
        default_app = paster.get_app(conf, 'main')
    app = default_app
    return app


def refresh():
    model.DBSession.flush()
    model.DBSession.execute('REFRESH TABLE tweets')


def setUp(test, app_func=get_app):
    app = app_func()
    testapp = TestApp(app)
    test.globs['app'] = testapp
    test.globs['refresh'] = refresh
    test.globs['pprint'] = pprint

    with open(schema_sql) as f:
        try:
            model.DBSession.execute(f.read().split(';')[0])
        except:
            pass


def create_suite(testfile, layer=None,
                 optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
                 level=None,
                 **kwargs):
    s = doctest.DocFileSuite(
        testfile, setUp=setUp,
        optionflags=optionflags,
        **kwargs
        )
    if layer:
        s.layer = layer
    if level:
        s.level = level
    return s


def test_suite():
    suites = (
        create_suite('probe_status.rst', layer=testing.crate_layer),
        create_suite('views.rst', layer=testing.crate_layer),
        )
    return unittest.TestSuite(suites)
