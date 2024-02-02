# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoListWidgetOption.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 447)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(30, 110, 431, 271))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButtonAdd = QtWidgets.QPushButton(Dialog)
        self.pushButtonAdd.setGeometry(QtCore.QRect(380, 60, 81, 31))
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonEdit = QtWidgets.QPushButton(Dialog)
        self.pushButtonEdit.setGeometry(QtCore.QRect(30, 400, 81, 31))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.pushButtonDelete = QtWidgets.QPushButton(Dialog)
        self.pushButtonDelete.setGeometry(QtCore.QRect(200, 400, 81, 31))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.pushButtonDeleteAll = QtWidgets.QPushButton(Dialog)
        self.pushButtonDeleteAll.setGeometry(QtCore.QRect(380, 400, 81, 31))
        self.pushButtonDeleteAll.setObjectName("pushButtonDeleteAll")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(200, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonAdd.setText(_translate("Dialog", "Add"))
        self.pushButtonEdit.setText(_translate("Dialog", "Edit"))
        self.pushButtonDelete.setText(_translate("Dialog", "Delete"))
        self.pushButtonDeleteAll.setText(_translate("Dialog", "Delete All"))
        self.label.setText(_translate("Dialog", "Todo List"))

