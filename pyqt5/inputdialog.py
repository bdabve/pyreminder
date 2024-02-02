#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 24.callInputDialog.py
|      CREATED : 09-août-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : input dialog
|        USAGE : ./24.callInputDialog.py
\ ====================================================================================================
"""

"""
[*] The input dialog box
An input dialog box is created with the help of the QInputDialog class.
The QInputDialog class provides a dialog to get a single value from the user.
The provided input dialog consists of a text field and two buttons, OK and Cancel.
The text field enables us to get a single value from the user, where that single value can be a string, a number, or an item from a
list.

[+] The following are the methods provided by the QInputDialog class to accept different types of input from the user:
    - getInt(): This method shows a spin box for accepting an integer number.
                To get an integer from the user, you need to use the following syntax:
                - getInt(self, window title, label before LineEdit widget, default value, minimum, maximum and step size)
                Example: quantity, ok = QInputDialog.getInt(self, "Order Quantity", "Enter quantity:", 2, 1, 100, 1)
    - getDouble(): This method shows a spin box with a floating point number to accept fractional values.
                To get a fractional value from the user, you need to use the following syntax:
                - getDouble(self, window title, label before LineEdit widget, default value, minimum, maximum and number of decimal places desired)
                  Example: price, ok = QInputDialog.getDouble(self, "Price of the product", "Enter price:", 1.50,0, 100, 2)
    - getText(): This method shows a Line Edit widget to accept text from the user.
                 To get text from the user, you need to use the following syntax:
                - getText(self, window title, label before LineEdit widget)
                  Example: name, ok = QtGui.QInputDialog.getText(self, 'Get Customer Name', 'Enter your name:')
    - getItem(): This method shows a combo box displaying several items to choose from.
                 - To get an item from a drop-down box, you need to use the following syntax:
                 - getItem(self, window title, label before combo box, array , current item, Boolean Editable)
                   Example: countryName, ok = QInputDialog.getItem(self, "Input Dialog", "List of countries", countries, 0, False)
"""
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog, QInputDialog
from demoInputDialog import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonCountry.clicked.connect(self.desp_msg)

        self.show()

    def desp_msg(self):
        countries = ('Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria')
        country_name, ok = QInputDialog.getItem(self, 'Input Dialog', 'List of countries', countries, 0, False)
        if ok and country_name:
            self.ui.lineEditCountry.setText(country_name)


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
