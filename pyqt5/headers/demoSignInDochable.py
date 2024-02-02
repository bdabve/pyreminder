# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/demoSignInDockable.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(90, 20, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 67, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 67, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(90, 80, 181, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 120, 181, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(180, 170, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Dockable Sign In Form"))
        self.label.setText(_translate("MainWindow", "Sign in"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Sign in"))
