# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoListWidget1.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 281)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 50, 191, 31))
        self.label.setObjectName("label")
        self.labelTest = QtWidgets.QLabel(Dialog)
        self.labelTest.setGeometry(QtCore.QRect(70, 200, 441, 41))
        self.labelTest.setText("")
        self.labelTest.setObjectName("labelTest")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(250, 50, 291, 121))
        self.listWidgetDiagnosis.setObjectName("listWidgetDiagnosis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDiagnosis.addItem(item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Choose the Diagnosis Tests"))
        __sortingEnabled = self.listWidgetDiagnosis.isSortingEnabled()
        self.listWidgetDiagnosis.setSortingEnabled(False)
        item = self.listWidgetDiagnosis.item(0)
        item.setText(_translate("Dialog", "Urine Analysis $5"))
        item = self.listWidgetDiagnosis.item(1)
        item.setText(_translate("Dialog", "Chest X Ray 100$"))
        item = self.listWidgetDiagnosis.item(2)
        item.setText(_translate("Dialog", "Sugar Level Text  $3"))
        item = self.listWidgetDiagnosis.item(3)
        item.setText(_translate("Dialog", "Hemoglobin Test $7"))
        item = self.listWidgetDiagnosis.item(4)
        item.setText(_translate("Dialog", "Thyroid Stimulating Harmone Test $10"))
        self.listWidgetDiagnosis.setSortingEnabled(__sortingEnabled)

