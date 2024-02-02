#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog, QColorDialog
from PyQt5.QtGui import QColor
from headers.demoColorDialog import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        col = QColor(0, 0, 0)               # set the color to black
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())       # set the color to the frame
        self.ui.pushButtonColor.clicked.connect(self.disp_msg)
        self.ui.pushButtonCopy.clicked.connect(self.copy_color)

        self.show()

    def disp_msg(self):
        col = QColorDialog.getColor()           # opens up a dialog showing defferent colors to choose.
        if col.isValid():
            self.ui.frameColor.setStyleSheet("QWidget { background-color: %s }" % col.name())       # set the color to the frame
            self.ui.pushButtonCopy.setText(str(col.name()))
            self.ui.pushButtonCopy.setEnabled(True)

    def copy_color(self):
        import pyperclip
        text = self.ui.pushButtonCopy.text()
        pyperclip.copy(text)


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
