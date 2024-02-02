#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 14.callFontComboBox.py
|      CREATED : 08-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : usage of comboBox font widget
|        USAGE : ./14.callFontComboBox.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtGui
from demoFontComboBox import *


class MyFormt(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # change the initial font for our application
        my_font = QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()), 15)
        # self.ui.fontComboBox.currentIndex()                                     # return the index of choosen object from fontComboBox
        # self.ui.fontComboBox.currentText(self.ui.fontComboBox.currentIndex())   # return the text from that index
        self.ui.textEdit.setFont(my_font)                                         # finally set the font to the textEdit

        # if font change than call the change_font method
        self.ui.fontComboBox.currentFontChanged.connect(self.change_font)

        self.show()

    def change_font(self):
        # after changing a font from the fontComboBox; then change it in text edit
        my_font = QtGui.QFont(self.ui.fontComboBox.itemText(self.ui.fontComboBox.currentIndex()), 15)
        self.ui.textEdit.setFont(my_font)


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyFormt()
    w.show()
    exit(app.exec_())
