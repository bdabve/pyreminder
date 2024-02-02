# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoListWidget2.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(571, 291)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.listWidgetSelectedTests = QtWidgets.QListWidget(Dialog)
        self.listWidgetSelectedTests.setGeometry(QtCore.QRect(290, 100, 271, 131))
        self.listWidgetSelectedTests.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidgetSelectedTests.setObjectName("listWidgetSelectedTests")
        self.listWidgetDiagnosis = QtWidgets.QListWidget(Dialog)
        self.listWidgetDiagnosis.setGeometry(QtCore.QRect(10, 100, 271, 131))
        self.listWidgetDiagnosis.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
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
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 121, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 60, 131, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
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
        self.label.setText(_translate("Dialog", "Diagnosis Tests"))
        self.label_2.setText(_translate("Dialog", "Selected tests are"))

