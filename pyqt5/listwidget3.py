#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoListWidget3 import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonAdd.clicked.connect(self.add_list)

        self.show()

    def add_list(self):
        self.ui.listWidgetSelectedItems.addItem(self.ui.lineEditFoodItem.text())
        self.ui.lineEditFoodItem.clear()
        self.ui.lineEditFoodItem.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
