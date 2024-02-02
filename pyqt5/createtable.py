#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callCreateTable.py
|      CREATED : 14-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : Create table in Sqlite3.
|        USAGE : ./callCreateTable.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
import sqlite3
from sqlite3 import Error
from createTable import *

table_definition = ""


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCreateTable.clicked.connect(self.create_table)
        self.ui.pushButtonAddColumn.clicked.connect(self.add_column)

        self.show()

    def add_column(self):
        global table_definition
        table_name = self.ui.lineEditTableName.text()
        column_name = self.ui.lineEditColumnName.text()
        data_type = self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex())

        if table_definition == "":
            table_definition = "CREATE TABLE IF NOT EXISTS {}( {} {}".format(table_name, column_name, data_type)
        else:
            table_definition += ', ' + self.ui.lineEditColumnName.text() + " " + self.ui.comboBoxDataType.itemText(self.ui.comboBoxDataType.currentIndex())

        self.ui.lineEditColumnName.clear()
        self.ui.lineEditColumnName.setFocus()

    def create_table(self):
        global table_definition
        try:
            conn = sqlite3.connect(self.ui.lineEditDbName.text() + '.db')
            self.ui.labelResult.setText('Database is connected')
            curs = conn.cursor()
            table_definition += ');'
            print(table_definition)
            curs.execute(table_definition)
            self.ui.labelResult.setText('Table is successfully created')
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
