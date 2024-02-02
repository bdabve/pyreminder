# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoBrowser.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(635, 564)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 40, 51, 31))
        self.label.setObjectName("label")
        self.lineEditUrl = QtWidgets.QLineEdit(Dialog)
        self.lineEditUrl.setGeometry(QtCore.QRect(70, 40, 471, 31))
        self.lineEditUrl.setObjectName("lineEditUrl")
        self.pushButtonGo = QtWidgets.QPushButton(Dialog)
        self.pushButtonGo.setGeometry(QtCore.QRect(558, 40, 71, 31))
        self.pushButtonGo.setObjectName("pushButtonGo")
        self.widget = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 90, 621, 471))
        self.widget.setObjectName("widget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "URL"))
        self.pushButtonGo.setText(_translate("Dialog", "Go"))
