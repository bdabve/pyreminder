#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 22.callMultilevelInheritance.py
|      CREATED : 09-août-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : multi level inheritance
|        USAGE : ./22.callMultilevelInheritance.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from demoMultilevelInheritance import *


class Student():
    name = ""
    code = ""

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name


class Marks(Student):
    history_marks = 0
    geography_marks = 0

    def __init__(self, name, code, history_marks, geography_marks):
        Student.__init__(self, name, code)
        self.history_marks = history_marks
        self.geography_marks = geography_marks

    def get_historyMarks(self):
        return history_marks

    def get_geographyMarks(self):
        return geography_marks


class Result(Marks):
    total_marks = 0
    percentage = 0

    def __init__(self, name, code, history_marks, geography_marks):
        Marks.__init__(self, name, code, history_marks, geography_marks)
        self.total_marks = history_marks + geography_marks
        self.percentage_marks = (self.history_marks + self.geography_marks) / (200 * 100)

    def get_totalMarks(self):
        return self.total_marks

    def get_percentageMarks(self):
        return self.percentage_marks


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonClick.clicked.connect(self.disp_msg)

        self.show()

    def disp_msg(self):
        name = self.ui.lineEditName.text()
        code = self.ui.lineEditCode.text()
        history = int(self.ui.lineEditHistory.text())
        geography = int(self.ui.lineEditGeography.text())
        result_obj = Result(name, code, history, geography)

        self.ui.lineEditTotal.setText(str(result_obj.get_totalMarks()))
        self.ui.lineEditPercentage.setText(str(result_obj.get_percentageMarks()))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
