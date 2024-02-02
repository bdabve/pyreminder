# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoListWidget3.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 300)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        font.setItalic(False)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 40, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEditFoodItem = QtWidgets.QLineEdit(Dialog)
        self.lineEditFoodItem.setGeometry(QtCore.QRect(160, 40, 221, 31))
        self.lineEditFoodItem.setObjectName("lineEditFoodItem")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(390, 40, 75, 31))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.listWidgetSelectedItems = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedItems.setGeometry(QtCore.QRect(15, 90, 451, 192))
        self.listWidgetSelectedItems.setObjectName("listWidgetSelectedItems")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your Favourite food"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))

