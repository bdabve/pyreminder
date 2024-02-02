#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi el3arbi_@email.com
# created       :
#
# description   : how to use thread with list widget
# -----------------------------------------------------
from PyQt5.QtWidgets import QApplication, QDialog
from headers.h_listwidgetthread import Ui_Dialog
import time, random
from threading import Thread


class ListWidgetThread(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.display)
        self.names = ['boujakji', 'Ja3boub', '3awd sahra', 'moh chalba', 'bouderbala', 'chakboub', 'eljam3i']

    def display(self):
        threadObj = Thread(target=self.get_items)
        threadObj.start()

    def get_items(self):
        count = 0
        for i in range(5000):
            self.ui.listWidget.addItem(str(random.choice(self.names)))
            time.sleep(0.01)
            count += 0.01
            self.ui.progressBar.setValue(int(count))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = ListWidgetThread()
    w.show()
    sys.exit(app.exec_())
