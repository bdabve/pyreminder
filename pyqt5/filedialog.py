#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 26.callFileDialog.py
|      CREATED : 10-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : Using of a main window with Menu and a file dialog to open and save a file
|        USAGE : ./26.callFileDialog.py
\ ====================================================================================================
"""

"""
- getOpenFileName() : This method opens the file dialog, enabling the user to browse the directories and open the desired file.
The syntax of the getOpenFileName() method is as follows:
    - file_name = QFileDialog.getOpenFileName(self, dialog_title, path, filter)
      filter represents the file extensions; it determines the types of file displayed to open, for example as follows:
        - file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home') # Shows all the files of home directory to browse from.
        - file_name = QFileDialog.getOpenFileName(self, 'Open file', '/home', "Images (*.png *.jpg);;Text files (.txt);;XML files (*.xml)")
            The files with the extensions .png , .jpg , .txt , and .xml will be displayed in the dialog box.

- getSaveFileName() : This method opens the file save dialog, enabling the user to save the file with the desired name and in the desired folder.
The syntax of the getSaveFileName() method is as follows:
    - file_name = QFileDialog.getSaveFileName(self, dialog_title, path, filter, options)
    - file_name, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","" ,"All Files (*);;Text Files (*.txt)", options=options)
        - The File Save dialog box will be opened allowing you to save the files with the desired extension.
        - If you don't specify the file extension, then it will be saved with the default extension, .txt.
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from demoFileDialog import *


class MyForm(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.open_file_dialog)
        self.ui.actionSave.triggered.connect(self.save_file_dialog)

        self.show()

    def open_file_dialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', '/home/dabve/programming/python')
        if fname[0]:                            # fname[0] contain the file name
            with open(fname[0], 'r') as f:
                data = f.read()
                self.ui.textEdit.setText(data)

    def save_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, 'QFileDialog.getSaveFileName()', '', 'All Files (*);;Text Files(*.txt)', options=options)
        with open(file_name, 'w') as f:
            text = self.ui.textEdit.toPlainText()
            f.write(text)
            f.close()


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
