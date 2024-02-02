# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoRadioButton2.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_secondExample(object):
    def setupUi(self, secondExample):
        secondExample.setObjectName("secondExample")
        secondExample.resize(632, 474)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        secondExample.setFont(font)
        self.label = QtWidgets.QLabel(secondExample)
        self.label.setGeometry(QtCore.QRect(50, 20, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(secondExample)
        self.label_2.setGeometry(QtCore.QRect(60, 200, 291, 31))
        self.label_2.setObjectName("label_2")
        self.labelSelected = QtWidgets.QLabel(secondExample)
        self.labelSelected.setGeometry(QtCore.QRect(70, 390, 361, 41))
        self.labelSelected.setText("")
        self.labelSelected.setObjectName("labelSelected")
        self.verticalLayoutWidget = QtWidgets.QWidget(secondExample)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 60, 231, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonMedium = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonMedium.setObjectName("radioButtonMedium")
        self.verticalLayout.addWidget(self.radioButtonMedium)
        self.radioButtonLarge = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonLarge.setObjectName("radioButtonLarge")
        self.verticalLayout.addWidget(self.radioButtonLarge)
        self.radioButtonXl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonXl.setObjectName("radioButtonXl")
        self.verticalLayout.addWidget(self.radioButtonXl)
        self.radioButtonXxl = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonXxl.setObjectName("radioButtonXxl")
        self.verticalLayout.addWidget(self.radioButtonXxl)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(secondExample)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 240, 231, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonDebitCard = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonDebitCard.setObjectName("radioButtonDebitCard")
        self.verticalLayout_2.addWidget(self.radioButtonDebitCard)
        self.radioButtonNetBanking = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonNetBanking.setObjectName("radioButtonNetBanking")
        self.verticalLayout_2.addWidget(self.radioButtonNetBanking)
        self.radioButtonCashOnDelivery = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButtonCashOnDelivery.setObjectName("radioButtonCashOnDelivery")
        self.verticalLayout_2.addWidget(self.radioButtonCashOnDelivery)

        self.retranslateUi(secondExample)
        QtCore.QMetaObject.connectSlotsByName(secondExample)

    def retranslateUi(self, secondExample):
        _translate = QtCore.QCoreApplication.translate
        secondExample.setWindowTitle(_translate("secondExample", "Dialog"))
        self.label.setText(_translate("secondExample", "Choose Your Shirt Size"))
        self.label_2.setText(_translate("secondExample", "Choose Your Payment Method"))
        self.radioButtonMedium.setText(_translate("secondExample", "M"))
        self.radioButtonLarge.setText(_translate("secondExample", "L"))
        self.radioButtonXl.setText(_translate("secondExample", "XL"))
        self.radioButtonXxl.setText(_translate("secondExample", "XXL"))
        self.radioButtonDebitCard.setText(_translate("secondExample", "Debit/Credit Card"))
        self.radioButtonNetBanking.setText(_translate("secondExample", "NetBanking"))
        self.radioButtonCashOnDelivery.setText(_translate("secondExample", "Cash On Delivery"))
