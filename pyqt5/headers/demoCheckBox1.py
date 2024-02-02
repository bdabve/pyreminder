# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 263)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(12)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 0, 201, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 261, 31))
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(90, 190, 261, 41))
        self.labelAmount.setObjectName("labelAmount")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(360, 70, 181, 23))
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlive = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlive.setGeometry(QtCore.QRect(360, 100, 191, 23))
        self.checkBoxOlive.setObjectName("checkBoxOlive")
        self.checkBoxSausage = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausage.setGeometry(QtCore.QRect(360, 130, 191, 23))
        self.checkBoxSausage.setObjectName("checkBoxSausage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra topping"))
        self.labelAmount.setText(_translate("Dialog", "TextLabel"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra Cheese $1"))
        self.checkBoxOlive.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxSausage.setText(_translate("Dialog", "Extra Sausages $2"))
