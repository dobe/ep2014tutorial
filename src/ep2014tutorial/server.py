from pyramid.config import Configurator
from pyramid.settings import aslist, asbool
from pyramid import security
from pyramid.authentication import AuthTktAuthenticationPolicy
from sqlalchemy import create_engine
from sqlalchemy import engine_from_config

from .model import DBSession, Base
from sqlalchemy.orm import sessionmaker


def app_factory(global_config, **settings):
    config = Configurator(settings=settings,
                          autocommit=True)
    config.include('ep2014tutorial.views')
    config.scan('ep2014tutorial.views')
    db_init(config)
    return config.make_wsgi_app()

def db_init(config):
    settings = config.get_settings()
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
