# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoClient.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 502)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setGeometry(QtCore.QRect(488, 450, 91, 31))
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.lineEditMsg = QtWidgets.QLineEdit(Dialog)
        self.lineEditMsg.setGeometry(QtCore.QRect(22, 450, 451, 31))
        self.lineEditMsg.setObjectName("lineEditMsg")
        self.textEditMsg = QtWidgets.QTextEdit(Dialog)
        self.textEditMsg.setGeometry(QtCore.QRect(20, 60, 451, 381))
        self.textEditMsg.setObjectName("textEditMsg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Client"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))
