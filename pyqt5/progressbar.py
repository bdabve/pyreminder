#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from headers.demoProgressBar import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.progressBar.setProperty("value", 0)                 # set the value to zero or you can maket it with
        # self.ui.progressBar.setValue(0)
        self.ui.pushButtonDownload.clicked.connect(self.update_bar)

        self.show()

    def update_bar(self):
        count = 0
        while count < 100:
            count += 0.0001
            self.ui.progressBar.setValue(int(count))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
