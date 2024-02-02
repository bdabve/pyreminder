#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : updating_data.py
#      CREATED : 12-November-2019
#       AUTHOR : daBve, dabve@outlook.fr
#
#         DESC : UPDATE, DELETE Data with SQLAlchemy
#        USAGE : ./updating_data.py
# ====================================================================================================
from sqlalchemy import create_engine, update
from create_tables import cookies, login
from sqlalchemy.sql import select

engine = create_engine('postgresql+psycopg2://dabve:sqlUbuntu@localhost:5432/dabve', pool_recycle=3600)
conn = login(engine)

# UPDATE
query = update(cookies).where(cookies.c.cookie_name == 'chocolate chip').values(quantity=(cookies.c.quantity + 120))
rows = conn.execute(query)
print(rows.rowcount)

query = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rows = conn.execute(query).first()
for row in rows.keys():
    print('{:>20}: {}'.format(row, rows[row]))

# DELETE
from sqlalchemy import delete
from sqlalchemy import and_

query = delete(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
rows = conn.execute(query)
print(rows.rowcount, 'records deleted successfully')        # returns 1 records deleted successfully

query = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
row = conn.execute(query).fetchall()
print(len(row), 'records with name: "dark chocolate chip"')     # return 0

# Delete with and_()
query = delete(cookies).where(and_(cookies.c.cookie_name == 'chocolate chip', cookies.c.cookie_id == '4'))
rows = conn.execute(query)
print(rows.rowcount)
