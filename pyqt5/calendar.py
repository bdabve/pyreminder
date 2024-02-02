#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
[*] Displaying a calendar
In order to enable the user to select a date, you need to display a monthly calendar.
Calendar Widget in Qt Designer helps in doing so.
This widget is an instance of the QCalendarWidget class that displays the current month and year by default and can be changed if desired.
The days appear in short form (Sun, Mon, Tue, and so on), and Saturday and Sunday are marked in red. Also, Sunday is displayed as the first
column in the calendar.

[+] Use the following properties of Calendar Widget to configure its display:
   - minimumDate           : This property is used for specifying the minimum date range.
   - maximumDate           : This property is used for specifying the maximum date range.
   - selectionMode         : This property helps in enabling or disabling the user's ability to select a date from Calendar Widget.
                             If this property is set to NoSelection, it will not allow the user to select any date.
   - verticalHeaderFormat  : You can remove the week numbers from Calendar Widget by setting this property to NoVerticalHeader.
   - gridVisible           : This property helps in making the calendar grid visible or invisible. You can set this property to the                             Boolean value True to make the calendar grid visible.
   - HorizontalHeaderFormat: This property is used for setting the days format to be displayed. Available options:
       - SingleLetterDayNames  : A single letter for days is displayed in the header, such as M for Monday, T for Tuesday.
       - ShortDayNames         : The short form of days are displayed in the header, such as Mon for Monday, Tue for Tuesday.
       - LongDayNames          : The header displays days in complete forms, such as Monday, Tuesday, and so on.
       - NoHorizontalHeader    : Using this option in HorizontalHeaderFormat makes the header invisible.

[+] The methods provided by QCalendarWidget are given in the following list:
    - selectedDate()        : This method returns the currently selected date. The date is returned as a QDate object.
    - monthShown()          : This method returns the currently displayed month.
    - yearShown()           : This method returns the currently displayed year.
    - setFirstDayOfWeek()   : This method is used to set the day of the week in the first column.
    - selectionChanged()    : This method is invoked when the user changes the currently selected date.

[*] The QDate class provides methods to extract the year, month, and day from the QDate instance.
    Using the QDate class The QDate class helps in handling dates.
    The instance of the QDate class accesses the date from the system clock
    and displays the date, which includes the year, month, and day, using the Gregorian calendar.

[+] The following is the list of methods provided by the QDate class:
    - currentDate() : This method returns the system date as a QDate instance.
    - setDate()     : This method sets the date based on the supplied year, month, and day.
    - year()        : This method returns the year from the specified QDate instance.
    - month()       : This method returns the month from the specified QDate instance.
    - day()         : This method returns the day from the specified QDate instance.
    - dayOfWeek()   : This method returns the day of the week from the specified QDate instance.
    - addDays()     : This method adds the specified number of days to the specified date and returns the new date.
    - addMonths()   : This method adds the specified number of months to the specified date and returns the new date.
    - addYears()    : This method adds the specified number of years to the specified date and returns the new date.
    - daysTo()      : This method returns the number of days between two dates.
    - daysInMonth() : This method returns the number of days in the specified month.
    - daysInYear()  : This method returns the number of days in the specified year.
    - isLeapYear()  : This method returns true if the specified date is in a leap year.
    - toPyDate()    : This method returns the date as a string. The format parameter determines the format of the result string.

[+] The following expressions are used for specifying the format:
    - d     : This expression displays the day as a number without a leading zero (1 to 31)
    - dd    : This expression displays the day as a number with a leading zero (01 to 31)
    - ddd   : This expression displays the day in short format (Mon, Tue, and so on)
    - dddd  : This expression displays the day in long format (Monday, Tuesday, and so on)
    - M     : This expression displays the month as a number without a leading zero (1 to 12)
    - MM    : This expression displays the month as a number with a leading zero (01 to 12)
    - MMM   : This expression displays the month in short format (Jan, Feb, and so on)
    - MMMM  : This expression displays the month in long format (January, February, and so on)
    - yy    : This expression displays the year as a two-digit number (00 to 99)
    - yyyy  : This expression displays the year as a four-digit number

[+] The properties used to configure the Date Edit widget are as follows:
    - minimumDate: A minimum date can be defined for the widget by making use of this property
    - maximumDate: A maximum date can be defined for the widget by making use of this property

[+] The following are the methods provided by the QDateEdit class:
    - setDate() : This method is used to set the date to be displayed in the widget
    - setDisplayFormat() : This method is used to set the date format for the date being displayed in the Date Edit widget

[+] The formats, with their output, are as follows:
    - dd.MM.yyyy    15.01.2018
    - MMM d yy      Jan 15 18
    - MMM d yyyy    Jan 15 2018
    - MMMM d yy     January 15 18
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from headers.demoCalendar import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.dateEdit.setDisplayFormat('dd MMM yyyy')
        self.ui.calendarWidget.selectionChanged.connect(self.desp_date)
        # set the day to single letter day name
        self.ui.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.SingleLetterDayNames)
        # no vertical header
        self.ui.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)

        self.show()

    def desp_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
