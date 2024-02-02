#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callInsertRow.py
|      CREATED : 14-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : insert a new row
|        USAGE : ./callInsertRow.py
\ ====================================================================================================
"""

import sqlite3
from sqlite3 import Error
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from demoInsertRow import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonInsert.clicked.connect(self.insert_row)

        self.show()

    def insert_row(self):
        db_name = self.ui.lineEditDbname.text()
        table_name = self.ui.lineEditTable.text()
        name = self.ui.lineEditName.text()
        email = self.ui.lineEditEmail.text()
        passwd = self.ui.lineEditPasswd.text()
        query = 'INSERT INTO ' + table_name + '(name, email, passwd) VALUES(?, ?, ?)'
        try:
            conn = sqlite3.connect(db_name + '.db')
            with conn:
                curs = conn.cursor()
                curs.execute(query, [name, email, passwd])
                self.ui.labelResult.setText('Row successfully inserted.')
                conn.commit()
        except Error as err:
            self.ui.labelResult.setText('Error: {}'.format(err))
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
