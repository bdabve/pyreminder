# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCalcutor.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 340)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.labelFirstN = QtWidgets.QLabel(Dialog)
        self.labelFirstN.setGeometry(QtCore.QRect(30, 70, 141, 20))
        self.labelFirstN.setObjectName("labelFirstN")
        self.labelSecondN = QtWidgets.QLabel(Dialog)
        self.labelSecondN.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.labelSecondN.setObjectName("labelSecondN")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(130, 210, 301, 31))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.lineEditFirstN = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirstN.setGeometry(QtCore.QRect(180, 70, 241, 31))
        self.lineEditFirstN.setObjectName("lineEditFirstN")
        self.lineEditSecondN = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecondN.setGeometry(QtCore.QRect(180, 140, 241, 31))
        self.lineEditSecondN.setObjectName("lineEditSecondN")
        self.pushButtonDivid = QtWidgets.QPushButton(Dialog)
        self.pushButtonDivid.setGeometry(QtCore.QRect(330, 270, 61, 31))
        self.pushButtonDivid.setObjectName("pushButtonDivid")
        self.pushButtonMultiply = QtWidgets.QPushButton(Dialog)
        self.pushButtonMultiply.setGeometry(QtCore.QRect(230, 270, 61, 31))
        self.pushButtonMultiply.setObjectName("pushButtonMultiply")
        self.pushButtonSubtract = QtWidgets.QPushButton(Dialog)
        self.pushButtonSubtract.setGeometry(QtCore.QRect(130, 270, 61, 31))
        self.pushButtonSubtract.setObjectName("pushButtonSubtract")
        self.pushButtonPlus = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlus.setGeometry(QtCore.QRect(30, 270, 61, 31))
        self.pushButtonPlus.setObjectName("pushButtonPlus")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(160, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 216, 67, 31))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelFirstN.setText(_translate("Dialog", "First number"))
        self.labelSecondN.setText(_translate("Dialog", "Second number"))
        self.pushButtonDivid.setText(_translate("Dialog", "/"))
        self.pushButtonMultiply.setText(_translate("Dialog", "x"))
        self.pushButtonSubtract.setText(_translate("Dialog", "-"))
        self.pushButtonPlus.setText(_translate("Dialog", "+"))
        self.labelTitle.setText(_translate("Dialog", "Calculator"))
        self.label.setText(_translate("Dialog", "Result"))
