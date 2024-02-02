# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\demoInputDialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 116)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.pushButtonCountry = QtWidgets.QPushButton(Dialog)
        self.pushButtonCountry.setGeometry(QtCore.QRect(390, 40, 151, 31))
        self.pushButtonCountry.setObjectName("pushButtonCountry")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 31))
        self.label.setObjectName("label")
        self.lineEditCountry = QtWidgets.QLineEdit(Dialog)
        self.lineEditCountry.setGeometry(QtCore.QRect(150, 40, 211, 31))
        self.lineEditCountry.setObjectName("lineEditCountry")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonCountry.setText(_translate("Dialog", "Choose Country"))
        self.label.setText(_translate("Dialog", "Your Country"))

