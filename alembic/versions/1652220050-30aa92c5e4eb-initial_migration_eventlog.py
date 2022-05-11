"""Initial Migration - EventLog

Revision ID: 30aa92c5e4eb
Revises: 
Create Date: 2022-05-10 15:00:50.531284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Column, CHAR, DECIMAL, VARCHAR, TIMESTAMP, JSON, Index

revision = '30aa92c5e4eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('event_log',
                    Column('id', DECIMAL(12, 6), primary_key=True),
                    Index('event_log_pk', 'id'),
                    Column('name', VARCHAR(30)),
                    Column('data', JSON()),
                    Column('timestamp', CHAR(48)),
                    Index('event_log_timestamp', 'timestamp')
                    )


    op.create_table('synchrony_log',
                    Column('id', DECIMAL(12, 6), primary_key=True),
                    Index('synchrony_log_pk', 'id'),
                    Column('aggregate', VARCHAR(30)),
                    Column('keyValue', JSON()),
                    Column('recordId', DECIMAL(12,6)),
                    Column('timestamp', CHAR(48)),
                    Index('synchrony_log_timestamp', 'timestamp')
                    )


def downgrade():
    pass
