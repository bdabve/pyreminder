#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from headers.demoCalcutor import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonPlus.clicked.connect(self.addTwoNum)
        self.ui.pushButtonSubtract.clicked.connect(self.subtractTwoNum)
        self.ui.pushButtonMultiply.clicked.connect(self.multiplyTwoNum)
        self.ui.pushButtonDivid.clicked.connect(self.dividTwoNum)

        self.show()

    def addTwoNum(self):
        if len(self.ui.lineEditFirstN.text()) != 0:
            a = int(self.ui.lineEditFirstN.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondN.text()) != 0:
            b = int(self.ui.lineEditSecondN.text())
        else:
            b = 0
        summ = a + b
        self.ui.labelResult.setText(str(summ))

    def subtractTwoNum(self):
        if len(self.ui.lineEditFirstN.text()) != 0:
            a = int(self.ui.lineEditFirstN.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondN.text()) != 0:
            b = int(self.ui.lineEditSecondN.text())
        else:
            b = 0
        diff = a - b
        self.ui.labelResult.setText(str(diff))

    def multiplyTwoNum(self):
        if len(self.ui.lineEditFirstN.text()) != 0:
            a = int(self.ui.lineEditFirstN.text())
        else:
            a = 1
        if len(self.ui.lineEditSecondN.text()) != 0:
            b = int(self.ui.lineEditSecondN.text())
        else:
            b = 1
        mult = a * b
        self.ui.labelResult.setText(str(mult))

    def dividTwoNum(self):
        if len(self.ui.lineEditFirstN.text()) != 0:
            a = int(self.ui.lineEditFirstN.text())
        else:
            a = 0
        if len(self.ui.lineEditSecondN.text()) != 0:
            b = int(self.ui.lineEditSecondN.text())
        else:
            b = 0
        divid = a / b
        self.ui.labelResult.setText(str(round(divid, 2)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
