# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_files\client.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEditMsg = QtWidgets.QTextEdit(Dialog)
        self.textEditMsg.setObjectName("textEditMsg")
        self.verticalLayout.addWidget(self.textEditMsg)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditSendMsg = QtWidgets.QLineEdit(Dialog)
        self.lineEditSendMsg.setObjectName("lineEditSendMsg")
        self.horizontalLayout.addWidget(self.lineEditSendMsg)
        self.pushButtonSend = QtWidgets.QPushButton(Dialog)
        self.pushButtonSend.setObjectName("pushButtonSend")
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Client"))
        self.pushButtonSend.setText(_translate("Dialog", "Send"))

