#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv, exit
from os.path import exists
import sqlite3
from PyQt5.QtWidgets import QApplication, QDialog
from sqlite3 import Error
from createSqliteDB import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCreate.clicked.connect(self.create_db)

        self.show()

    def create_db(self):
        db_name = self.ui.lineEditDBName.text() + '.db'
        if exists(db_name):
            self.ui.labelResult.setText('Database already exist.')
        else:
            try:
                conn = sqlite3.connect(db_name)
                self.ui.labelResult.setText('Database created successfully.')
            except Error as e:
                self.ui.labelResult.setText('Errro: {}'.format(e))
            finally:
                if conn:
                    conn.close()


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
