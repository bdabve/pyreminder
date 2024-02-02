# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(516, 238)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(6, 70, 261, 51))
        self.label.setObjectName("labelResponse")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(60, 130, 101, 31))
        self.labelResponse.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(160, 80, 231, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.buttonClickMe = QtWidgets.QPushButton(Dialog)
        self.buttonClickMe.setGeometry(QtCore.QRect(260, 170, 131, 41))
        self.buttonClickMe.setObjectName("buttonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your name "))
        self.labelResponse.setText(_translate("Dialog", "Response"))
        self.buttonClickMe.setText(_translate("Dialog", "Click"))
