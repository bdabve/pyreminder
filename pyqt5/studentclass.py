#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 20.callLineEditClass.py
|      CREATED : 09-août-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : application based on classes
|        USAGE : ./20.callLineEditClass.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from demoStudentClass import *


class Student:
    name = ''

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.lineEditCode.setFocus()
        self.ui.ButtonClickMe.clicked.connect(self.disp_msg)

        self.show()

    def disp_msg(self):
        student_obj = Student(self.ui.lineEditCode.text(), self.ui.lineEditName.text())
        self.ui.labelResponse.setText('Student Code: {}\nStudent name: {}'.format(student_obj.get_code(), student_obj.get_name()))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
