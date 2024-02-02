#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog, QFontDialog
from demoFontDialog import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonFont.clicked.connect(self.change_font)

        self.show()

    def change_font(self):
        font, ok = QFontDialog.getFont()
        print(font.family())
        if ok:
            self.ui.textEdit.setFont(font)


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
