#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 21.callDemoSimpleIngeritance.py
|      CREATED : 09-août-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : simple inheritance
|        USAGE : ./21.callDemoSimpleIngeritance.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from demoSimpleInheritance import *


class Student:

    code = ''
    name = ''

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name


class Marks(Student):
    hostory_marks = 0
    geographi_marks = 0

    def __init__(self, code, name, history_marks, geography_marks):
        Student.__init__(self, code, name)
        self.history_marks = history_marks
        self.geography_marks = geography_marks

    def get_historyMarks(self):
        return self.history_marks

    def get_geographyMarks(self):
        return self.geography_marks


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.ButtonClickMe.clicked.connect(self.disp_msg)

        self.show()

    def disp_msg(self):
        code = self.ui.lineEditCode.text()
        name = self.ui.lineEditName.text()
        history = self.ui.lineEditHistory.text()
        geography = self.ui.lineEditGeography.text()
        mark_obj = Marks(code, name, history, geography)
        self.ui.labelResponse.setText('Student Code: {}, Student Name: {}\nHistory Marks: {}, Geography Marks: {}'.format(mark_obj.get_code(), mark_obj.get_name(), mark_obj.get_historyMarks(), mark_obj.get_geographyMarks()))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
