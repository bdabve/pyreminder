#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from headers.demoCheckBox1 import *

"""
[*] Method application

The following are the methods provided by the QCheckBox class:
  - isChecked() : This method returns the Boolean value true if the checkbox is checked, and otherwise returns false.
  - setTristate() : If you don't want the user to change the state of the checkbox, you pass the Boolean value true to this method.
                    The user will not be able to check or uncheck the checkbox.
  - setIcon() : This method is used to display an icon with the checkbox.
  - setText() : This method assigns text to the checkbox. To specify a shortcut key for the checkbox,
                precede the preferred character in the text with an ampersand. The shortcut character will appear as underlined.
  - setChecked() : In order to make a checkbox appear as checked by default, pass the Boolean value true to this method.

[*] Signal description

The signals emitted by QCheckBox are as follows:
    - clicked(): This signal is emitted when a checkbox is activated (that is, pressed and released) or when its shortcut key is pressed
    - stateChanged(): This signal is emitted whenever a checkbox changes its state from checked to unchecked or vice versa
"""


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlive.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausage.stateChanged.connect(self.dispAmount)

        self.show()

    def dispAmount(self):
        amount = 10
        checked = "Nothings"

        if self.ui.checkBoxCheese.isChecked() is True:
            print(self.ui.checkBoxCheese.text())
            amount = amount + 1
            checked = "Cheese"
        if self.ui.checkBoxOlive.isChecked() is True:
            amount = amount + 1
            checked = "Olive"
        if self.ui.checkBoxSausage.isChecked() is True:
            amount = amount + 2
            checked = "Sausages"

        self.ui.labelAmount.setText('Pizza with {}: {}'.format(checked, amount))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
