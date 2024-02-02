#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callSelectRows.py
|      CREATED : 15-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : display database rows in a table
|        USAGE : ./callSelectRows.py
\ ====================================================================================================
"""

from sys import argv, exit
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from demoSelectRows import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.setRowCount(5)              # modifying row numbers
        self.ui.pushButtonDisplayRows.clicked.connect(self.display_rows)

        self.show()

    def display_rows(self):
        db_name = self.ui.lineEditDbName.text() + '.db'
        table_name = self.ui.lineEditTblName.text()
        query = 'SELECT * FROM ' + table_name
        try:
            conn = sqlite3.connect(db_name)
            curs = conn.cursor()
            curs.execute(query)
            rows = curs.fetchall()
            print(rows)
            # rowNo = 0
            for index, row in enumerate(rows):
                self.ui.labelResult.setText('Number of rows in {}: {}'.format(table_name, str(len(rows))))
                colNo = 0
                for column in row:
                    oneColumn = QTableWidgetItem(column)
                    self.ui.tableWidget.setItem(index, colNo, oneColumn)
                    colNo += 1
                # rowNo += 1
        except Error as err:
            self.ui.tableWidget.clear()
            self.ui.labelResult.setText('Error: {}'.format(err))
        finally:
            if conn:
                conn.close()


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
