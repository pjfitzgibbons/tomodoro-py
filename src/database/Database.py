from sqlalchemy import create_engine, Column, JSON, DECIMAL, Table, Index, VARCHAR, CHAR
from sqlalchemy.orm import Session

from database.Base import metadata

PROD_URI = 'sqlite:///tomodoro.sqlite'
TEST_URI = 'sqlite://'


class Database:
    def db_init(self, uri):
        self.engine = create_engine(uri or PROD_URI)

        self.init_tables()
        metadata.create_all(self.engine)
        self.connection = self.engine.connect()

    def test_init(self):
        self.db_init(TEST_URI)

    @staticmethod
    def init_tables():
        Database.EventLog = Table('event_log', metadata,
                                  Column('id', DECIMAL(12, 6), primary_key=True),
                                  Index('event_log_pk', 'id'),
                                  Column('name', VARCHAR(30)),
                                  Column('data', JSON()),
                                  Column('timestamp', CHAR(48)),
                                  Index('event_log_timestamp', 'timestamp'))

    def session(self):
        return Session(self.engine)
