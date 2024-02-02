#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton2 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_secondExample()
        self.ui.setupUi(self)

        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXl.toggled.connect(self.dispSelected)
        self.ui.radioButtonXxl.toggled.connect(self.dispSelected)

        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)

        self.show()

    def dispSelected(self):
        selected1 = ""
        selected2 = ""
        if self.ui.radioButtonMedium.isChecked():
            selected1 = 'Medium'
        if self.ui.radioButtonLarge.isChecked():
            selected1 = 'Large'
        if self.ui.radioButtonXl.isChecked():
            selected1 = 'Extra Large'
        if self.ui.radioButtonXxl.isChecked():
            selected1 = 'Extra Extra Large'

        if self.ui.radioButtonDebitCard.isChecked():
            selected2 = 'Debit/Credit Card'
        if self.ui.radioButtonNetBanking.isChecked():
            selected2 = 'Net Banking'
        if self.ui.radioButtonCashOnDelivery.isChecked():
            selected2 = 'Cash On Delivery'

        self.ui.labelSelected.setText('Shirt size: {}\nPayment method: {}'.format(selected1, selected2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
