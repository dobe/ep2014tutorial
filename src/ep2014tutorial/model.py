from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
import uuid

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

def genuuid():
    return str(uuid.uuid4())

