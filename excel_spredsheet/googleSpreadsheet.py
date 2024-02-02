#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# DESCRIPTION: This script show how to work with spreadsheet stored in gdrive
# From: "https://www.youtube.com/watch?v=vISRn5qFrkM&list=WL"
# ----------------------------------------------------------------------------

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# use creds to create a client to interact with google drive api
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('lagislators-ff9694e5f5fb.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
sheet = client.open("Copy of Legislators 2017").sheet1

# Extract and print all the value
pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
# pp.pprint(result)

row6 = sheet.row_values(6)
# pp.pprint(row6)

col6 = sheet.col_values(6)
# pp.pprint(col6)

cell = sheet.cell(6, 11)
pp.pprint(cell)

# Updating an existing cell
sheet.update_cell(6, 11, '555-867-5309')
cell = sheet.cell(6, 11)
pp.pprint(cell)

# Create our own row from python
row = ["I'm", "Updating", "a", "spreadsheet", "from", "Python!"]
index = 3
sheet.insert_row(row, index)

# Delete row
sheet.delete_row(3)

# Find out the total number of rows
print(sheet.row_count)
