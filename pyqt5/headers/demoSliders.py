# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demoSliders.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(481, 381)
        font = QtGui.QFont()
        font.setFamily("Monaco")
        font.setPointSize(9)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 30, 111, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 91, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(280, 120, 91, 21))
        self.label_4.setObjectName("label_4")
        self.lineEditResult = QtWidgets.QLineEdit(Dialog)
        self.lineEditResult.setGeometry(QtCore.QRect(40, 300, 411, 41))
        self.lineEditResult.setObjectName("lineEditResult")
        self.horizontalScrollBarSugarLevel = QtWidgets.QScrollBar(Dialog)
        self.horizontalScrollBarSugarLevel.setGeometry(QtCore.QRect(200, 30, 241, 21))
        self.horizontalScrollBarSugarLevel.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarSugarLevel.setObjectName("horizontalScrollBarSugarLevel")
        self.verticalScrollBarPulseRate = QtWidgets.QScrollBar(Dialog)
        self.verticalScrollBarPulseRate.setGeometry(QtCore.QRect(190, 120, 16, 160))
        self.verticalScrollBarPulseRate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarPulseRate.setObjectName("verticalScrollBarPulseRate")
        self.horizontalSliderBloodPressure = QtWidgets.QSlider(Dialog)
        self.horizontalSliderBloodPressure.setGeometry(QtCore.QRect(200, 70, 241, 19))
        self.horizontalSliderBloodPressure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBloodPressure.setObjectName("horizontalSliderBloodPressure")
        self.verticalSliderCholestrolLevel = QtWidgets.QSlider(Dialog)
        self.verticalSliderCholestrolLevel.setGeometry(QtCore.QRect(420, 120, 19, 160))
        self.verticalSliderCholestrolLevel.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderCholestrolLevel.setObjectName("verticalSliderCholestrolLevel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Sugar Level"))
        self.label_2.setText(_translate("Dialog", "Blood Pressure"))
        self.label_3.setText(_translate("Dialog", "Pulse rate"))
        self.label_4.setText(_translate("Dialog", "Cholesterol"))

