# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoSpinBox.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 275)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(380, 190, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(10)
        self.labelTotalAmount.setFont(font)
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(300, 30, 42, 31))
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(300, 110, 62, 31))
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(170, 30, 113, 31))
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(380, 30, 131, 31))
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(170, 110, 113, 31))
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(380, 110, 131, 31))
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", " Book Price value"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))

