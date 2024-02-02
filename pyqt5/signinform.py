#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callSigninForm.py
|      CREATED : 15-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : sign in form
|        USAGE : ./callSigninForm.py
\ ====================================================================================================
"""

from sys import argv, exit
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QDialog
from demoSigninForm import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.pushButtonSignIn.clicked.connect(self.signin)

        self.show()

    def signin(self):
        email = self.ui.lineEditEmail.text()
        passwd = self.ui.lineEditPassword.text()
        query = 'SELECT email, passwd FROM Users WHERE email = ? AND passwd = ?'
        try:
            conn = sqlite3.connect('pyqtExample.db')
            curs = conn.cursor()
            curs.execute(query, [email, passwd])
            row = curs.fetchone()
            if row is None:
                self.ui.labelResult.setText('Sorry, Incorrect email address or password')
            else:
                self.ui.labelResult.setText('You Are Welcome')
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
