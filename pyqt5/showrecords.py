#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callShowRecords.py
|      CREATED : 15-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : show records
|        USAGE : ./callShowRecords.py
\ ====================================================================================================
"""

from sys import argv, exit
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog
from demoShowRecords import *

rowNo = 1
query = 'SELECT name, email, passwd FROM Users'
conn = sqlite3.connect('pyqtExample.db')
curs = conn.cursor()


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        curs.execute(query)
        self.ui.pushButtonFirst.clicked.connect(self.first_row)
        self.ui.pushButtonLast.clicked.connect(self.last_row)
        self.ui.pushButtonNext.clicked.connect(self.next_row)
        self.ui.pushButtonPrev.clicked.connect(self.prev_row)

        self.show()

    def first_row(self):
        try:
            curs.execute(query)
            row = curs.fetchone()
            if row:
                self.ui.lineEditName.setText(row[0])
                self.ui.lineEditEmail.setText(row[1])
                self.ui.lineEditPasswd.setText(row[2])
        except Error as err:
            self.ui.labelResult.setText('Error: {}'.format(err))

    def prev_row(self):
        global rowNo
        rowNo -= 1
        query = 'SELECT name, email, passwd FROM Users WHERE row_id = ?'
        curs.execute(query, [rowNo])
        row = curs.fetchone()
        if row:
            self.ui.labelResult.clear()
            self.ui.lineEditName.setText(row[0])
            self.ui.lineEditEmail.setText(row[1])
            self.ui.lineEditPasswd.setText(row[2])
        else:
            rowNo += 1
            self.ui.labelResult.setText('This is the first row')

    def next_row(self):
        global rowNo
        rowNo += 1
        query = 'SELECT name, email, passwd FROM Users WHERE row_id = ?'
        curs.execute(query, [rowNo])
        row = curs.fetchone()
        if row:
            self.ui.labelResult.clear()
            self.ui.lineEditName.setText(row[0])
            self.ui.lineEditEmail.setText(row[1])
            self.ui.lineEditPasswd.setText(row[2])
        else:
            rowNo -= 1
            self.ui.labelResult.setText('This is the last row')

    def last_row(self):
        curs.execute(query)
        for row in curs.fetchall():
            self.ui.lineEditName.setText(row[0])
            self.ui.lineEditEmail.setText(row[1])
            self.ui.lineEditPasswd.setText(row[2])


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
