# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\demoMultipleInheritance.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 376)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(10)
        font.setItalic(False)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 141, 31))
        self.label_2.setObjectName("label_2")
        self.labelHistory = QtWidgets.QLabel(Dialog)
        self.labelHistory.setGeometry(QtCore.QRect(30, 130, 141, 31))
        self.labelHistory.setObjectName("labelHistory")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 210, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 250, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEditCode = QtWidgets.QLineEdit(Dialog)
        self.lineEditCode.setGeometry(QtCore.QRect(200, 50, 241, 31))
        self.lineEditCode.setObjectName("lineEditCode")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(200, 90, 241, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditHistory = QtWidgets.QLineEdit(Dialog)
        self.lineEditHistory.setGeometry(QtCore.QRect(200, 130, 241, 31))
        self.lineEditHistory.setObjectName("lineEditHistory")
        self.lineEditGeography = QtWidgets.QLineEdit(Dialog)
        self.lineEditGeography.setGeometry(QtCore.QRect(200, 170, 241, 31))
        self.lineEditGeography.setObjectName("lineEditGeography")
        self.lineEditTotal = QtWidgets.QLineEdit(Dialog)
        self.lineEditTotal.setEnabled(False)
        self.lineEditTotal.setGeometry(QtCore.QRect(200, 210, 241, 31))
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.lineEditPercentage = QtWidgets.QLineEdit(Dialog)
        self.lineEditPercentage.setEnabled(False)
        self.lineEditPercentage.setGeometry(QtCore.QRect(200, 250, 241, 31))
        self.lineEditPercentage.setObjectName("lineEditPercentage")
        self.pushButtonClick = QtWidgets.QPushButton(Dialog)
        self.pushButtonClick.setGeometry(QtCore.QRect(334, 310, 101, 31))
        self.pushButtonClick.setObjectName("pushButtonClick")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Student Code"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.labelHistory.setText(_translate("Dialog", "History Mark"))
        self.label_3.setText(_translate("Dialog", "Geography Mark"))
        self.label_5.setText(_translate("Dialog", "Total"))
        self.label_6.setText(_translate("Dialog", "Percentage"))
        self.pushButtonClick.setText(_translate("Dialog", "Click"))

