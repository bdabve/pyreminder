#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To display several values in an easier and expandable format, you can use List Widget, which is an instance of the QListWidget class.
List Widget displays several items that can not only be viewed, but can be edited and deleted, too.
You can add or remove list items one at a time from the List Widget item, or collectively you can set list items by using its
internal model.

[*] Items in the list are instances of the QListWidgetItem class.
The methods provided by QListWidget are shown in the following list:
    - insertItem()      : Inserts a new item with the supplied text into List Widget at the specified location.
    - insertItems()     : Inserts multiple items from the supplied list, starting at the specified location.
    - count()           : Returns the count of the number of items in the list.
    - takeItem()        : Removes and returns items from the specified row in List Widget.
    - currentItem()     : Returns the current item in the list.
    - setCurrentItem()  : Replaces the current item in the list with the specified item.
    - addItem()         : Appends the item with the specified text at the end of List Widget.
    - addItems()        : Appends items from the supplied list at the end of List Widget.
    - clear()           : Removes all items from List Widget.
    - currentRow()      : Returns the row number of the current selected list item.
                          If no list item is selected, it returns the value -1.
    - setCurrentRow()   : Selects the specified row in List Widget.
    - item()            : Returns the list item at the specified row.

[*] Signals emitted by the QListWidget class are shown in the following list:
    - currentRowChanged()   : This signal is emitted when the row of the current list item changes
    - currentTextChanged()  : This signal is emitted whenever the text in the current list item is changed
    - currentItemChanged()  : This signal is emitted when the focus of the current list item is changed
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from headers.demoListWidget1 import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.listWidgetDiagnosis.itemClicked.connect(self.dispSelectedTest)

        self.show()

    def dispSelectedTest(self):
        self.ui.labelTest.setText('You have selected: {}'.format(self.ui.listWidgetDiagnosis.currentItem().text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
