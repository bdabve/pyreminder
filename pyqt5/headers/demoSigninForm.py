# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoSigninForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 372)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 101, 31))
        self.label_3.setObjectName("label_3")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(140, 110, 271, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(140, 160, 271, 31))
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonSignIn = QtWidgets.QPushButton(Dialog)
        self.pushButtonSignIn.setGeometry(QtCore.QRect(318, 220, 91, 31))
        self.pushButtonSignIn.setObjectName("pushButtonSignIn")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(20, 300, 381, 41))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sign in"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButtonSignIn.setText(_translate("Dialog", "Sign in"))
