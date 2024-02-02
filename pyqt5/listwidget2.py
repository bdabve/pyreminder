#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoListWidget2 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.listWidgetDiagnosis.itemSelectionChanged.connect(self.dispSelectedTest)
        self.show()

    def dispSelectedTest(self):
        self.ui.listWidgetSelectedTests.clear()
        items = self.ui.listWidgetDiagnosis.selectedItems()
        for item in list(items):
            self.ui.listWidgetSelectedTests.addItem(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
