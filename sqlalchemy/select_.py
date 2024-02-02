#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# FILE     :
# AUTHOR   : daBve, dabve@gmail.com
# CREATED  :
# UPDATED  :
# -----------------------------------------------------
# REQ      :
# DESC     :
# -----------------------------------------------------

from sqlalchemy import create_engine
from create_tables import login, orders     # , users     # cookies
from terminaltables import AsciiTable

engine = create_engine('sqlite:///sql_alchemy.sqlite')
conn = login(engine)


def display_table(rp, method='first'):
    table_data = [rp.keys()]                         # append description as table headers

    if method == 'first':
        result = rp.first()
        table_data.append(result)
    elif method == 'fetchone':
        result = rp.fetchone()
        table_data.append(result)
    else:
        result = rp.fetchall()
        for row in result:
            table_data.append(row)

    table_instance = AsciiTable(table_data)
    print(table_instance.table)


from sqlalchemy import select
columns = [orders.c.order_id, users.c.username, users.c.phone, cookies.c.cookie_name, line_items.c.quantity,
           line_items.c.extended_cost ]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join)
display_table(rp, 'fetchall')       # display result in table
