# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\demoStudentClass.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 238)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(10)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 60, 111, 31))
        self.label.setObjectName("label")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(140, 60, 211, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(20, 110, 331, 41))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(240, 180, 111, 31))
        self.ButtonClickMe.setObjectName("ButtonClickMe")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(16, 20, 111, 31))
        self.label_2.setObjectName("label_2")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(140, 20, 211, 31))
        self.lineEditCode.setObjectName("lineEditCode")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
        self.label_2.setText(_translate("Dialog", "Student Code"))

