# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoInsertRow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(446, 410)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 131, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 131, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 131, 21))
        self.label_5.setObjectName("label_5")
        self.lineEditDbname = QtWidgets.QLineEdit(Dialog)
        self.lineEditDbname.setGeometry(QtCore.QRect(170, 80, 241, 25))
        self.lineEditDbname.setObjectName("lineEditDbname")
        self.lineEditTable = QtWidgets.QLineEdit(Dialog)
        self.lineEditTable.setGeometry(QtCore.QRect(170, 120, 241, 25))
        self.lineEditTable.setObjectName("lineEditTable")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(170, 160, 241, 25))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(170, 200, 241, 25))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPasswd = QtWidgets.QLineEdit(Dialog)
        self.lineEditPasswd.setGeometry(QtCore.QRect(170, 240, 241, 25))
        self.lineEditPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswd.setObjectName("lineEditPasswd")
        self.pushButtonInsert = QtWidgets.QPushButton(Dialog)
        self.pushButtonInsert.setGeometry(QtCore.QRect(288, 300, 121, 25))
        self.pushButtonInsert.setObjectName("pushButtonInsert")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(30, 356, 381, 31))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(150, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Database Name"))
        self.label_2.setText(_translate("Dialog", "Table Name"))
        self.label_3.setText(_translate("Dialog", "Name"))
        self.label_4.setText(_translate("Dialog", "Email"))
        self.label_5.setText(_translate("Dialog", "Password"))
        self.pushButtonInsert.setText(_translate("Dialog", "Insert Row"))
        self.label_6.setText(_translate("Dialog", "Insert Row"))
