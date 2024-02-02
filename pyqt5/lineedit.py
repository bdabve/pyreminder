#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : callLineEdit.py
|      CREATED : 06-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : this file call the ./demoLineEdit.py designed with PyQt5 designer
|        USAGE : ./callLineEdit.py
\ ====================================================================================================
"""

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from demoLineEdit import *

"""
[* ]Methods
The following are the methods provided by the QLineEdit class:

    - setEchoMode() : It sets the echo mode of the Line Edit widget. That is, it determines how the contents of the Line Edit widget are to be
                      displayed. The available options are as follows:
        - Normal : This is the default mode and it displays characters the way they are entered
        - NoEcho : It switches off the Line Edit echo, that is, it doesn't display anything
        - Password : Used for password fields, no text will be displayed; instead, asterisks appear for the text entered by the user
        - PasswordEchoOnEdit : It displays the actual text while editing the password fields, otherwise it will display the asterisks for the text

    - maxLength() : This method is used to specify the maximum length of text that can be entered in the Line Edit widget.
    - setText() : This method is used for assigning text to the Line Edit widget.
    - text() : This method accesses the text entered in the Line Edit widget.
    - clear() : This method clears or deletes the complete content of the Line Edit widget.
    - setReadOnly() : When the Boolean value true is passed to this method, it will make the Line Edit widget read-only, that is, non-editable.
                      The user cannot make any changes to the contents displayed through the Line Edit widget, but can only copy.
    - isReadOnly() : This method returns the Boolean value true if the Line Edit widget is in read-only mode, otherwise it returns false.
    - setEnabled() : By default, the Line Edit widget is enabled, that is, the user can make changes to it.
                     But if the Boolean value false is passed to this method, it will disable the Line Edit widget so the user cannot edit
                    its content, but can only assign text via the setText() method.
    - setFocus() : This method positions the cursor on the specified Line Edit widget.

[*] Understanding the Push Button widget
    To display a push button in an application, you need to create an instance of the QPushButton class.
    When assigning text to buttons, you can create shortcut keys by preceding any character in the text with an ampersand.
    For example, if the text assigned to a push button is Click Me , the character C will be underlined to indicate that it is a
    shortcut key, and the user can select the button by pressing Alt + C. The button emits the clicked() signal if it is activated.
    Besides text, an icon can also be displayed in the push button.
    The methods for displaying text and an icon in a push button are as follows:
        - setText() : This method is used to assign text to the push button
        - setIcon() : This method is used to assign an icon to the push button
"""


class MyForm(QDialog):      # ingerits from the base class QDialog.
    def __init__(self):     # the default constructor fro QDialog. the defautl constructor has no parent, is known as a window
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Handling the event
        # Event in PyQt5 uses signals and slots.
        # A signal is an event, and a slot is a method that is executed on the occurence of a signal.
        # Example: when you click a push button, a clicked() event, also known as a signal, occurs,
        #          the connect() method connect signals with slots.

        # self.ui.lineEditName.setEchoMode(QLineEdit.Password)      # you must import QLineEdit
        # self.ui.lineEditName.setFocus()
        self.ui.buttonClickMe.clicked.connect(self.dispmessage)

        self.show()

    def dispmessage(self):
        self.ui.labelResponse.setText('Hello ' + self.ui.lineEditName.text())
        self.ui.lineEditName.clear()            # Clear text after clicking the push button


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())       # the sys.exit() methid ensures a clean exit, releasing memory resoures.
