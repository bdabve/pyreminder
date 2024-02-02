#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[*] Table Widget
Table Widget is used for displaying data in tabular format, arranged in rows and columns.
Table Widget is an instance of the QTableWidget class and the items that are displayed in the different rows and columns of a table
are instances of the QTableWidgetItem class.
[+] Methods provided by the QTableWidget class:
    - setRowCount()     : This method is used to define the number of rows you want in Table Widget
    - setColumnCount()  : This method is used to define the number of columns required in Table Widget
    - rowCount()        : This method returns the number of rows in the table
    - columnCount()     : This method returns the number of columns in the table
    - clear()           : This method clears the entire table
    - setItem()         : This method sets the content for a given row and column of the table

[*] The QTableWidgetItem class
As mentioned earlier, the items displayed in Table Widget are instances of the QTableWidgetItem class.
You can display text, images, or any other widgets as items in Table Widget.

[+] Methods provided by the QTableWidgetItem class:
    - setFont()         : This method sets the font for the text label of the Table Widget item
    - setCheckState()   : This method passes the Boolean value True to this method to check the table item and passes the value
                          False to uncheck the Table Widget item
    - checkState()      : This method returns the Boolean value as True if the Table Widget item is checked, or otherwise returns False
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem
from demoTableWidget import *


class MyForm(QDialog):

    def __init__(self, data):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.data = data
        self.add_content()

    def add_content(self):
        for row, tupl in enumerate(self.data):
            col = 0
            for item in tupl:
                one_item = QTableWidgetItem(item)               # convert item var into an instance of QTableWidgetItem
                self.ui.tableWidget.setItem(row, col, one_item)
                col += 1


if __name__ == '__main__':
    app = QApplication(argv)
    data = []
    data.append(('Suite', '40'))
    data.append(('Super Luxury', '30'))
    data.append(('Super Deluxe', '20'))
    data.append(('Ordinary', '20'))
    w = MyForm(data)
    w.show()
    exit(app.exec_())
