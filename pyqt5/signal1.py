#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 6.callSignal1.py
|      CREATED : 06-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : Copy text from one QLineEdit to another one
|        USAGE : ./6.callSignal1.py
\ ====================================================================================================
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoSignal1 import *

"""
QtCore : The QtCore module forms the foundation of all Qt-based applications.
         It contains the most fundamental classes, such as QCoreApplication , QObject , and so on.
        These classes do important tasks, such as event handling, implementing the signal and slot mechanism, I/O operations, handling strings,
        and so on. The module includes several classes, including QFile , QDir , QIODevice , QTimer , QString , QDate , and QTime .
QtGui : As the name suggests, the QtGUI module contains the classes required in developing cross-platform GUI applications.
        The module contains the GUI classes, such as QCheckBox , QComboBox , QDateTimeEdit , QLineEdit , QPushButton , QPainter , QPaintDevice ,
        QApplication , QTextEdit , and QTextDocument .
"""


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        """
        In PyQt, any widget can be used as a top-level window
        The super().__init() method invokes the base class constructor.
        in this code the constructor of the QDialog class is called, to indicate that QDialog is displayed through this class is a top-level window.
        """
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)       # set the user interface by calling the setupUi() method from the file created by PyQt5 designer
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
