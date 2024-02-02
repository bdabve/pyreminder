#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[*] A Spin Box widget can be created using two classes, QSpinBox and QDoubleSpinBox, where QSpinBox displays only integer values,
and the QDoubleSpinBox class displays floating-point values.

[*] Methods provided by QSpinBox are shown in the following list:
    - value(): This method returns the current integer value selected from the spin box.
    - text(): This method returns the text displayed by the spin box.
    - setPrefix(): This method assigns the prefix text that is prepended to the value returned by the spin box.
    - setSuffix(): This method assigns the suffix text that is to be appended to the value returned by the spin box.
    - cleanText(): This method returns the value of the spin box without a suffix, a prefix, or leading or trailing whitespaces.
    - setValue(): This method assigns the value to the spin box.
    - setSingleStep(): This method sets the step size of the spin box. Step size is the increment/decrement value of the spin box,
                        that is, it is the value by which the spin box's value will increase or decrease on selecting the up or down buttons.
    - setMinimum(): This method sets the minimum value of the spin box.
    - setMaximum(): This method sets the maximum value of the spin box.
    - setWrapping(): This method passes the Boolean value true to this method to enable wrapping in the spin box.
                     Wrapping means the spin box returns to the first value (minimum value) when the up button is pressed while displaying
                     the maximum value.

[*] Signals emitted by the QSpinBox class are as follows:
    - valueChanged(): This signal is emitted when the value of the spin box is changed either by selecting the up/down button or using
                      the setValue() method
    - editingFinished(): This signal is emitted when focus is lost on the spin box.
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from demoSpinBox import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBoxSugarWeight.editingFinished.connect(self.result2)

        self.show()

    def result1(self):
        if len(self.ui.lineEditBookPrice.text()) != 0:
            bookPrice = int(self.ui.lineEditBookPrice.text())
        else:
            bookPrice = 0

        totalBookAmount = self.ui.spinBoxBookQty.value() * bookPrice
        self.ui.lineEditBookAmount.setText(str(totalBookAmount))

    def result2(self):
        if len(self.ui.lineEditSugarPrice.text()) != 0:
            sugarPrice = float(self.ui.lineEditSugarPrice.text())
        else:
            sugarPrice = 0

        totalSugarAmount = self.ui.doubleSpinBoxSugarWeight.value() * sugarPrice
        self.ui.lineEditSugarAmount.setText(str(round(totalSugarAmount, 2)))

        totalBookAmount = int(self.ui.lineEditBookAmount.text())
        totalAmount = totalBookAmount + totalSugarAmount
        self.ui.labelTotalAmount.setText(str(round(totalAmount, 2)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
