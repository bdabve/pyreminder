#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# created : 16-June-2021
# desc    : How to use google sheets from python and pandas
# ---------------------------------------------------------
import pygsheets
# import pandas as pd
# import numpy as np

# Authorization
gc = pygsheets.authorize(service_account_file='./semiotic-primer-317013-8b1217446342.json')


# open the google spreadsheet by file name
sh = gc.open_by_key('1RpBer2ljh76s2-oR39gFtiYjpHYbgEPiynf1mezkja0')
# print(sh.id)
# print(sh.title)
# sh.delete()                       # delete spreadsheet

# sh.share('myfriend@gmail.com')    # share the sheet with friends
# sh.share('example@gmail.com', role='commenter', type='user', emailMessage='Here is the spreadsheet we talked about!')
# sh.share('', role='reader', type='anyone')        # make public

# ------------------------------
# create a new sheet
# sh.add_worksheet('Sheet3', rows=250, cols=20)
# print('done adding sheet: Sheet3')
# print(sh.worksheets())              # Return information of worksheets
# sh.del_worksheet('Sheet3')          # delete worksheet

# ------------------------------
# select the first sheet
wks = sh[1]     # or wks = sh.sheet1
# print(wks.title)
# print(wks.id)
# print(wks.url)
# print(wks.rows)       # number of rows
# print(wks.cols)       # number of cols
# wks.cell(row_number, col_number)            # returns cell object
# wks.cell(row_number, col_number).value      # returns cell value as string

# update a cell with value
# wks.update_value('A1', 'This is a test from python')

# print(wks.get_value('A1'))
# print(wks.get_value('A1', 'B2'))        # return list of value
# print(wks.get_all_value())              # return list of all values in worksheet
# print(wks.get_all_records())            # return list of dictionaries

wks.update_value('B1', '40')
wks.update_value('B3', '30')
wks.update_value('B4', '=B1+B3', True)

# update a cell with value
wks.update_value('A1', 'Hey yank this numpy array')
nparray = np.random.randint(10, size=(3, 4))
wks.update_values('A5', nparray.tolist())

# you want to fill height values of students
# header = wks.cell('A8')
# header.value = 'Names'
# header.text_format['bold'] = True
# header.update()
# or achive the same in oneliner
# wks.cell('B8').set_text_format('bold', True).value = 'heights'

# set the names
# wks.update_values('A9:A13', [['Dabve'], ['John'], ['Aplam'], ['Bahou'], ['Halala']])

# set the heights
# heights = wks.range("B9:B13", returnas='range')     # get the range as DataRange object
# heights.start = 'B9'
# heights.end = 'B13'
# heights.name = "heights"                                    # name the range
# heights.update_values([[50], [60], [67], [66], [77]])       # update the values
# wks.update_values('B13', '=average(heights)')               # set the avg value of heights using named range
