# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoComboBox.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(433, 192)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 161, 21))
        self.label.setObjectName("label")
        self.labelAccountType = QtWidgets.QLabel(Dialog)
        self.labelAccountType.setGeometry(QtCore.QRect(20, 120, 391, 31))
        self.labelAccountType.setText("")
        self.labelAccountType.setObjectName("labelAccountType")
        self.comboBoxAccountType = QtWidgets.QComboBox(Dialog)
        self.comboBoxAccountType.setGeometry(QtCore.QRect(190, 50, 221, 22))
        self.comboBoxAccountType.setObjectName("comboBoxAccountType")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")
        self.comboBoxAccountType.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select account type"))
        self.comboBoxAccountType.setItemText(0, _translate("Dialog", "Saving Account"))
        self.comboBoxAccountType.setItemText(1, _translate("Dialog", "Current Account"))
        self.comboBoxAccountType.setItemText(2, _translate("Dialog", "Recurring Deposit Account "))
        self.comboBoxAccountType.setItemText(3, _translate("Dialog", "Fixed Deposit Account"))

