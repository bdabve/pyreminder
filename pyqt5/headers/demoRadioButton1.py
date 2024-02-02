# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondQtExample(object):
    def setupUi(self, SecondQtExample):
        SecondQtExample.setObjectName("SecondQtExample")
        SecondQtExample.resize(400, 300)
        self.label = QtWidgets.QLabel(SecondQtExample)
        self.label.setGeometry(QtCore.QRect(10, 30, 371, 41))
        self.label.setObjectName("label")
        self.radioButtonFirstClass = QtWidgets.QRadioButton(SecondQtExample)
        self.radioButtonFirstClass.setGeometry(QtCore.QRect(30, 90, 161, 23))
        self.radioButtonFirstClass.setObjectName("radioButtonFirstClass")
        self.radioButtonBusinessClass = QtWidgets.QRadioButton(SecondQtExample)
        self.radioButtonBusinessClass.setGeometry(QtCore.QRect(30, 130, 181, 23))
        self.radioButtonBusinessClass.setObjectName("radioButtonBusinessClass")
        self.radioButtonEconomyClass = QtWidgets.QRadioButton(SecondQtExample)
        self.radioButtonEconomyClass.setGeometry(QtCore.QRect(30, 170, 181, 23))
        self.radioButtonEconomyClass.setObjectName("radioButtonEconomyClass")
        self.labelFare = QtWidgets.QLabel(SecondQtExample)
        self.labelFare.setGeometry(QtCore.QRect(30, 226, 341, 31))
        self.labelFare.setText("")
        self.labelFare.setObjectName("labelFare")

        self.retranslateUi(SecondQtExample)
        QtCore.QMetaObject.connectSlotsByName(SecondQtExample)

    def retranslateUi(self, SecondQtExample):
        _translate = QtCore.QCoreApplication.translate
        SecondQtExample.setWindowTitle(_translate("SecondQtExample", "Dialog"))
        self.label.setText(_translate("SecondQtExample", "                           Choose the flight type"))
        self.radioButtonFirstClass.setText(_translate("SecondQtExample", "First Class $150"))
        self.radioButtonBusinessClass.setText(_translate("SecondQtExample", "Business Class $125"))
        self.radioButtonEconomyClass.setText(_translate("SecondQtExample", "Economy Class $100"))
