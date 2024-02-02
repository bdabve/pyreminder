#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoRadioButton1 import *

"""
[*] Methods
The QRadioButton class provides the following methods:
    - isChecked() : This method returns the Boolean value true if the button is in the selected state.
    - setIcon() : This method displays an icon with the radio button.
    - setText() : This method assigns the text to the radio button. If you want to specify a shortcut key for the radio button,
                  precede the preferred character in the text with an ampersand ( & ). The shortcut character will be underlined.
    - setChecked() : To make any radio button appear selected by default, pass the Boolean value true to this method.

[*] Signal description
Signals emitted by QRadioButton are as follows:
    - toggled(): This signal is emitted whenever the button changes its state from checked to unchecked or vice versa
    - clicked(): This signal is emitted when a button is activated (that is, pressed and released) or when its shortcut key is pressed
    - stateChanged(): This signal is emitted when a radio button changes its state from checked to unchecked or vice versa
"""


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SecondQtExample()
        self.ui.setupUi(self)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)

        self.show()

    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked() is True:
            fare = 150
        if self.ui.radioButtonBusinessClass.isChecked() is True:
            fare = 125
        if self.ui.radioButtonEconomyClass.isChecked() is True:
            fare = 100

        self.ui.labelFare.setText('Air Fare is: ' + str(fare))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
