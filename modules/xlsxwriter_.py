#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
--------------------------------------------------------
FILE     : xlsxwriter_.py
CREATED  : 15-August-2020
AUTHOR   : daBve, dabve@outlook.fr
USAGE    : ./xlsxwriter_.py
----------------------------------------------------------------------------------------
DESC:
    XlsxWriter can be used to write text, numbers, formulas and hyperlinks to multiple
    worksheets and it supports features such as formatting and many more,
    It supports Python 2.7, 3.4+ and PyPy and uses standard libraries only.
----------------------------------------------------------------------------------------
"""
import xlsxwriter
import os
import sys
sys.path.extend(['../bin'])
from sqlite_functions import SqliteFunctions


def write_to_excel(fname, shname, db_name, query, params=()):
    """
    Export data from sqlite table to excel file.
        fname   == file.xlsx
        shname  == sheetname
        db_name == sqlite database
        query   == SQL query
        params  == params for the query
    """
    db_handler = SqliteFunctions(db_name)
    desc, rows = db_handler.makeQuery(query, params)

    if os.path.exists(fname):
        # if file with the same name; then remove
        os.remove(fname)

    with xlsxwriter.Workbook(fname) as wbook:
        wsheet = wbook.add_worksheet(shname)

        # Insert an image
        # worksheet.insert_image('B5', 'nameofimage.png')

        # formate rows
        desc_format = wbook.add_format({'font_name': 'Times New Roman',
                                        'bold': True,
                                        'font_size': 16,
                                        'border': 1,
                                        'align': 'center',
                                        'valign': 'center'})

        rows_format = wbook.add_format({'font_name': 'Times New Roman', 'font_size': 14, 'border': 1})
        # date_format = wbook.add_format({'num_format': 'dd mmmm yyyy'})
        # money_format = wbook.add_format({'num_format': '# ##0,00 €'})
        # wsheet.set_row(3, 25)               # set the height for row 3
        # wsheet.set_column('A:A', 25)        # set the length for column A:A (movement_date)

        # write title
        title = 'QUERY: {} => PARAMS: {}'.format(query, params)
        title_format = wbook.add_format({'font_name': 'Times New Roman',
                                         'font_size': 16,
                                         'bold': True,
                                         'italic': True,
                                         'align': 'center'})
        wsheet.merge_range('A1:I2', title, title_format)      # merge and write title

        # write description
        excel_row = 3
        excel_col = 0
        for des in desc:
            wsheet.write(excel_row, excel_col, des.title(), desc_format)
            excel_col += 1

        # write rows
        excel_row = 4
        for row in rows:
            excel_col = 0
            for r in row:
                wsheet.write(excel_row, excel_col, r, rows_format)
                excel_col += 1
            excel_row += 1
        print('Done writing to {}'.format(fname))


if __name__ == '__main__':
    fname = 'test.xlsx'
    shname = 'test_from_python'
    db_name = '../bin/db.sqlite'
    query = 'SELECT * FROM magasin_pdr LIMIT ?'
    params = [30]
    write_to_excel(fname, shname, db_name, query, params)
