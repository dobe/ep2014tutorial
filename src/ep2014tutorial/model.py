from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from crate.client.sqlalchemy.types import Object
from sqlalchemy import (Column,
                        String,
                        DateTime,
                        Boolean,
                        Integer)

import uuid

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

def genuuid():
    return str(uuid.uuid4())

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(String, primary_key=True)
    created_at = Column(DateTime)
    text = Column(String)
    source = Column(String)
    retweeted = Column(Boolean)

    user = Column(Object)

    def __json__(self, request):
        res =  dict(id=self.id,
                    text=self.text,
                    created_at=self.created_at.isoformat()
            )
        userId = self.user and self.user.get('id')
        if userId:
            res['user'] = userId
        return res
