#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
[*] Qt Designer enables us to display LCD-like digits of any size by making use of its LCD Number widget.
The LCD Number widget is an instance of the QLCDNumber class and it can be used to display decimal, hexadecimal, octal, and binary digits
of any size.
[+] The methods provided by QLCDNumber are as follows:
    - setMode(): This method is used to change the base of the numbers.

    [+] Available options are as follows:
        - Hex: This option is used to display hexadecimal digits
        - Dec: This option is used to display decimal digits
        - Oct: This option is used to display octal digits
        - Bin: This option is used to display binary digits

    - display(): This method is used to display the supplied data in LCD digit format.
    - value(): This method returns the numerical value displayed by the LCD Number widget.

[*] Using Timers
Timers are used for performing repetitive tasks. A timer is an instance of the QTimer class.
The task to be repeated needs to be written in a method and that method, in turn, is invoked via the timeout() signal of the QTimer instance.
The timeout() signal can be configured or adjusted using the following methods:
    - start(n)              : It compels the timer to generate the timeout() signal at n millisecond intervals
    - setSingleShot(true)   : It constrains the timer to generate the timeout() signal only once
    - singleShot(n)         : It makes the timer generate a timeout() signal only once, and that too after n milliseconds

[*] Using the QTime class
The QTime class not only helps in reading the current time from the system clock but also provides all clock time functions.
It shows time in terms of hours, minutes, seconds, and milliseconds since midnight.
Also, it helps in measuring the span of elapsed time.
The time returned by the QTime class is in 24-hour format. The methods provided by the QTime class are as follows:
    - currentTime() : This method accesses the system clock time and returns it as a QTime object
    - hour() : This method returns the number of hours
    - minute() : This method returns the number of minutes
    - seconds() : This method returns the number of seconds
    - msec() : This method returns the number of milliseconds
    - addSecs() : This method returns the time after adding the specified number of seconds
    - addMSecs() : This method returns the time after adding the specified number of milliseconds
    - secsTo() : This method returns the difference in the number of seconds between two QTime objects
    - msecsTo() : This method returns the difference in the number of milliseconds between two times
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from demoLCD import *


class MyForm(QDialog):

    def __init__(self):

        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        timer = QtCore.QTimer(self)                 # creating an instance of QTimer
        timer.timeout.connect(self.show_lcd)        # whenever timeout() is generated, the show_lcd method will be invoked.
        timer.start(1000)                           # every 1000 miliseconds generate a timeout() signal

        self.show_lcd()

    def show_lcd(self):
        time = QtCore.QTime.currentTime()           # fetch the current system clock time.
        text = time.toString('hh:mm')               # converting it to string and make it eppear in the HH:MM format.
        self.ui.lcdNumber.display(text)             # finally display it.


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
