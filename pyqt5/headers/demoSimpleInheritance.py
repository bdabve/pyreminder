# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\demoSimpleInheritance.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 416)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(170, 50, 211, 31))
        self.lineEditCode.setObjectName("lineEditCode")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 131, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 131, 31))
        self.label_4.setObjectName("label_4")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(170, 100, 211, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditHistory = QtWidgets.QLineEdit(Dialog)
        self.lineEditHistory.setGeometry(QtCore.QRect(170, 150, 211, 31))
        self.lineEditHistory.setObjectName("lineEditHistory")
        self.lineEditGeography = QtWidgets.QLineEdit(Dialog)
        self.lineEditGeography.setGeometry(QtCore.QRect(170, 200, 211, 31))
        self.lineEditGeography.setObjectName("lineEditGeography")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(260, 260, 121, 31))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(26, 330, 351, 41))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.label_3.setText(_translate("Dialog", "History Marks"))
        self.label_4.setText(_translate("Dialog", "Geography Marks"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))

