#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
List Widget consists of several list items.
These list items are instances of the QListWidgetItem class.
The list items can be inserted into List Widget using the insertItem() or addItem() methods.
List items may be in text or icon form and can be checked or unchecked.

[*] Methods provided by the QListWidgetItem class
Let's take a look at the following methods provided by the QListWidgetItem class:
    - setText()     : Assigns the specified text to the list item
    - setIcon()     : Assigns the specified icon to the list item
    - checkState()  : Returns the Boolean value depending on whether the list item is in a checked or unchecked state
    - setHidden()   : Passes the Boolean value true to this method to hide the list item
    - isHidden()    : Returns true if the list item is hidden
"""
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from demoListWidgetOption import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Adding some items with addItem() method
        self.ui.listWidget.addItem('Ice Cream')
        self.ui.listWidget.addItem('Sode')
        self.ui.listWidget.addItem('Coffe')
        self.ui.listWidget.addItem('Chocolate')

        # Dealing with our buttons
        self.ui.pushButtonAdd.clicked.connect(self.add_list)
        self.ui.pushButtonEdit.clicked.connect(self.edit_list)
        self.ui.pushButtonDelete.clicked.connect(self.del_item)
        self.ui.pushButtonDeleteAll.clicked.connect(self.del_all_items)

        self.show()

    def add_list(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()

    def edit_list(self):
        row = self.ui.listWidget.currentRow()
        newtext, ok = QInputDialog.getText(self, 'Enter new text', 'Enter new text')
        if ok and (len(newtext) != 0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row, QListWidgetItem(newtext))

    def del_item(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def del_all_items(self):
        self.ui.listWidget.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
