#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QUrl
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from headers.demoBrowser import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonGo.clicked.connect(self.disp_site)

        self.show()

    def disp_site(self):
        self.ui.widget.load(QUrl(self.ui.lineEditUrl.text()))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
