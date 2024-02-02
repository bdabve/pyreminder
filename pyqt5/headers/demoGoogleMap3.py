# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoGoogleMap3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(522, 300)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 40, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 141, 31))
        self.label_3.setObjectName("label_3")
        self.lineEditFirst = QtWidgets.QLineEdit(Dialog)
        self.lineEditFirst.setGeometry(QtCore.QRect(190, 94, 271, 31))
        self.lineEditFirst.setObjectName("lineEditFirst")
        self.lineEditSecond = QtWidgets.QLineEdit(Dialog)
        self.lineEditSecond.setGeometry(QtCore.QRect(190, 140, 271, 31))
        self.lineEditSecond.setObjectName("lineEditSecond")
        self.pushButtonFind = QtWidgets.QPushButton(Dialog)
        self.pushButtonFind.setGeometry(QtCore.QRect(328, 180, 131, 31))
        self.pushButtonFind.setObjectName("pushButtonFind")
        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setGeometry(QtCore.QRect(40, 240, 421, 31))
        self.labelResult.setText("")
        self.labelResult.setObjectName("labelResult")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Distance between two location"))
        self.label_2.setText(_translate("Dialog", "First Location"))
        self.label_3.setText(_translate("Dialog", "Second Location"))
        self.pushButtonFind.setText(_translate("Dialog", "Find Distance"))
