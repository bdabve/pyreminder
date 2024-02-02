#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : 18.callHotelReservation.py
|      CREATED : 08-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : a hotel room reservation app
|        USAGE : ./18.callHotelReservation.py
\ ====================================================================================================
"""

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from hotelReservation import *


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.room_type = ['Suite', 'Super Luxury', 'Super Deluxe', 'Ordinary']
        # self.ui.comboBox.addItems(self.room_type)         # we can add all items with addItems
        self.add_content()      # this methods add room_type to the comboBox widget

        self.ui.pushButton.clicked.connect(self.compute_room_rent)

        self.show()

    def add_content(self):
        for i in self.room_type:
            self.ui.comboBox.addItem(i)

    def compute_room_rent(self):
        selected_date = self.ui.calendarWidget.selectedDate()       # fetch the date of reservation
        dateInString = str(selected_date.toPyDate())                # convert it to PyDate and to a string
        noOfDays = self.ui.spinBox.value()                          # take the spinbox value number of days
        roomType = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())   # and take the room type from the comboBox
        # display information about the chosen option in enteredInfo label
        self.ui.enteredInfo.setText('Reservation date: {}, Number of Days: {}.\nRoom Type: {}'.format(dateInString, noOfDays, roomType))

        # calculating room type and number of days
        room_rent = 0
        if roomType == 'Suite':
            room_rent = 40
        elif roomType == 'Super Luxury':
            room_rent = 30
        elif roomType == 'Super Deluxe':
            room_rent = 20
        elif roomType == 'Ordinary':
            room_rent = 10
        total = room_rent * noOfDays

        # display the total rent in the roomRentInfo label
        self.ui.roomRentInfo.setText('Rent for single day for {} type is: {}.\nTotal: {}'.format(roomType, room_rent, total))


if __name__ == '__main__':
    app = QApplication(argv)
    w = MyForm()
    w.show()
    exit(app.exec_())
