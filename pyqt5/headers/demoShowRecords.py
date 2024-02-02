# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoShowRecords.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 355)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 91, 31))
        self.label_3.setObjectName("label_3")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(160, 60, 291, 31))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEditEmail.setGeometry(QtCore.QRect(160, 110, 291, 31))
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.lineEditPasswd = QtWidgets.QLineEdit(Dialog)
        self.lineEditPasswd.setGeometry(QtCore.QRect(160, 160, 291, 31))
        self.lineEditPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPasswd.setObjectName("lineEditPasswd")
        self.pushButtonFirst = QtWidgets.QPushButton(Dialog)
        self.pushButtonFirst.setGeometry(QtCore.QRect(30, 230, 89, 31))
        self.pushButtonFirst.setObjectName("pushButtonFirst")
        self.pushButtonLast = QtWidgets.QPushButton(Dialog)
        self.pushButtonLast.setGeometry(QtCore.QRect(360, 230, 89, 31))
        self.pushButtonLast.setObjectName("pushButtonLast")
        self.pushButtonNext = QtWidgets.QPushButton(Dialog)
        self.pushButtonNext.setGeometry(QtCore.QRect(250, 230, 89, 31))
        self.pushButtonNext.setObjectName("pushButtonNext")
        self.pushButtonPrev = QtWidgets.QPushButton(Dialog)
        self.pushButtonPrev.setGeometry(QtCore.QRect(140, 230, 89, 31))
        self.pushButtonPrev.setObjectName("pushButtonPrev")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(30, 290, 421, 31))
        self.labelResult.setText("")
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.labelTitle = QtWidgets.QLabel(Dialog)
        self.labelTitle.setGeometry(QtCore.QRect(170, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Name"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButtonFirst.setText(_translate("Dialog", "First"))
        self.pushButtonLast.setText(_translate("Dialog", "Last"))
        self.pushButtonNext.setText(_translate("Dialog", "Next"))
        self.pushButtonPrev.setText(_translate("Dialog", "Previous"))
        self.labelTitle.setText(_translate("Dialog", "Show Records"))
