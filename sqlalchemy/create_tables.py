#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : 1.create_tables.py
#      CREATED : 11-November-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : Connecting to database, and Creating Tables.
#                This file contain the basics of starting using SQLAlchemy;
#
#        USAGE : ./1.create_tables.py
# ====================================================================================================

from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean, CheckConstraint

# engine = create_engine('postgresql+psycopg2://dabve:sqlUbuntu@localhost:5432/dabve', pool_recycle=3600)
#                         db_type   +dialect ://user :passwd   @host     :port/dbname'
# Creting an engine for a remote MySQL database
# engine = create_engine('mysql+pymysql://cookiemonster:chocolatechip@mysql01.monster.internal/cookies', pool_recycle=3600)


def login(engine):
    try:
        conn = engine.connect()
    except Exception as err:
        return err
    else:
        return conn


"""
echo            : This will log the actions processed by the engine, such as SQL statements and their parameters. default=False
encoding        : This define the string encoding use by SQLAlchemy. default=True
isolation_level : This insructs SQLAlchemy to use a specific isolation level.
pool_recycle    : The recycles or times out the database connections at regular intervals.

# Generic type representations

| SQLAlchemy    | Python              | SQL
|---------------|---------------------|---------------------------
| BigInteger    | int                 | BIGINT
| Boolean       | bool                | BOOLEAN or SMALLINT
| Date          | datetime.date       | DATE (SQLite: STRING )
| DateTime      | datetime.datetime   | DATETIME (SQLite: STRING )
| Enum          | str                 | ENUM or VARCHAR
| Float         | float or Decimal    | FLOAT or REAL
| Integer       | int                 | INTEGER
| Interval      | datetime.timedelta  | INTERVAL or DATE from epoch
| LargeBinary   | byte                | BLOB or BYTEA
| Numeric       | decimal.Decimal     | NUMERIC or DECIMAL
| Unicode       | unicode             | UNICODE or VARCHAR
| Text          | str                 | CLOB or TEXT
| Time          | datetime.time       | DATETIME
"""

metadata = MetaData()
"""
Metadata is used to tie together the database structure so it can be quickly accessed inside SQLAlchemy.
It's often useful to think of metadata as a kind of catalog of Table object with optional information about the engine and conn.
Those tables can be accessed via a dictionary, MetaData.tables.
"""
cookies = Table('cookies', metadata,
                Column('cookie_id', Integer(), primary_key=True),
                Column('cookie_name', String(50), index=True),
                Column('cookie_recipe_url', String(255)),
                Column('cookie_sku', String(55)),
                Column('quantity', Integer()),
                Column('unit_cost', Numeric(12, 2)),
                CheckConstraint('quantity > 0', name='quantity_positive')
                )

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
              )

"""
# Declaring key after creations
  from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
  PrimaryKeyConstraint('user_id', name='user_pk')
  UniqueConstraint('username', name='uix_userame')

# Ensure that the data supplied for a column matches a set of user_defined criteria.
# In this example, ensuring the unit_cost is never allowed to be less than 0.00
  CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')

# Indexes
  from sqlalchemy import Index
  Index('index_name', 'column_name')
  Index('ix_cookies_cookie_name', 'cookie_name')

# ForeignKey after creation
  from sqlalchemy import ForeignKeyConstraint
  ForeignKeyConstraint(['order_id'], ['orders.order_id'])
"""

orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),  # ForeignKey on users.user_id
               Column('shipped', Boolean(), default=False)
               )

line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order_id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )

if __name__ == '__main__':
    # engine = create_engine('postgresql+psycopg2://dabve:sqlUbuntu@localhost:5432/dabve', pool_recycle=3600)
    engine = create_engine('sqlite:///sql_alchemy.sqlite')
    conn = login(engine)
    metadata.create_all(engine)         # Create all tables
    # Conditional by default, will not attempt to recreate tables already present in the target database.
    # lego_sets.append_column(Column('parent_id', Integer(), nullable=True))
    print('Done Adding all Tables')
