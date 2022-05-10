import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, JSON, DateTime, String, DECIMAL
from sqlalchemy.orm import declarative_base, Session

engine =  create_engine('sqlite:///tomodoro.sqlite', echo=True, future=True)

Base = declarative_base()


class EventLog(Base):
    __tablename__ = 'event_log'

    id = Column(String(), primary_key=True)
    name = Column(String())
    data = Column(JSON())
    timestamp = Column(DateTime(), nullable=False)
    epochMillis = Column(DECIMAL(36, 8), nullable=False)
    version = Column(String(), nullable=False)


Base.metadata.create_all(engine)
