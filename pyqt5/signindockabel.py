#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 30.callSignInDockabel.py
|      CREATED : 12-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : a dockable sign in form
|        USAGE : ./30.callSignInDockabel.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from demoSignInDochable import *


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(argv)
    w = AppWindow()
    w.show()
    exit(app.exec_())
