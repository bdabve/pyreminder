#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------
# FILE     : sqdb_to_excel.py
# CREATED  : 15-August-2020
# AUTHOR   : daBve, dabve@outlook.fr
# USAGE    : ./sqdb_to_excel.py
# ----------------------------------
# DESC     : Save a query result into xlsx file with pandas
# --------------------------------------------------------
import pandas as pd
import sys
sys.path.extend(['../bin'])
from sqlite_functions import SqliteFunctions

handler = SqliteFunctions('../bin/db.sqlite')
desc, rows = handler.makeQuery('select * from movement')                     # show as table

df = pd.DataFrame.from_records(data=rows, columns=desc)
writer = pd.ExcelWriter('etats_2020.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Etats')
wbook = writer.book
wsheet = writer.sheets['Etats']

# format headers
header_format = wbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#333',
    'border': 1
})

for desc, rows in enumerate(df.columns.values):
    wsheet.write(0, desc + 1, rows, header_format)

writer.save()
