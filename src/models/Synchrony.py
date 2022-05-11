from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from sqlalchemy.orm import Session

from database.Base import Base
from sqlalchemy import Column, Index, VARCHAR, JSON, DECIMAL, CHAR

def _default_timestamp():
    return datetime.now().isoformat()

def _default_id():
    return datetime.now().timestamp()

class Synchrony(Base):
    """

    >>> from database.Database import Database
    >>> s = Synchrony(aggregate=None, keyValue={ 'start': datetime.now() }, recordId=None)
    >>> s # doctest: +ELLIPSIS
    Synchrony(id=None, aggregate=None, keyValue={'start': datetime.datetime(...)}), recordId=None, timestamp=None)
    >>> db = Database()
    >>> db.test_init()
    >>> with db.session() as session:
    ...     session.add(s)
    ...     session.commit()
    >>> s
    True
    """
    __tablename__ = 'synchrony_log'
    id = Column(DECIMAL(12, 6), primary_key=True, default=_default_id )
    aggregate = Column(VARCHAR(30))
    keyValue = Column(JSON())
    recordId = Column(DECIMAL(12,6))
    timestamp = Column(CHAR(48), nullable=False, default=_default_timestamp )


    class Keys(Enum):
        START = 'start'

    def __repr__(self):
        return f"Synchrony(id={self.id!r}, aggregate={self.aggregate!r}, keyValue={self.keyValue!r}), recordId={self.recordId!r}, " \
               f"timestamp={self.timestamp!r})"
