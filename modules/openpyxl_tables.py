#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi el3arbi_@email.com
# created       :
#
# description   :
# usage         :
# ----------------------------------------------------------------------------


from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
wb = Workbook()
ws = wb.active
data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears', 2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges', 500, 300, 200, 700]
]

# add column headings. NB. these must be strings
ws.append(['Fruit', '2011', '2012', '2013', '2014'])
for row in data:
    ws.append(row)
table = Table(displayName="Table1", ref="A1:E5")
style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False, showLastColumn=False,
                       showRowStripes=True, showColumnStripes=True)
table.tableStyleInfo = style
ws.add_table(table)
wb.save('table_openpyxl.xlsx')
