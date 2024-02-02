#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QDialog
from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix
from headers.demoGoogleMap3 import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonFind.clicked.connect(self.disp_location)

        self.show()

    def disp_location(self):
        first_location = self.ui.lineEditFirst.text()
        second_location = self.ui.lineEditSecond.text()
        api_key = 'AIzaSyCQQZftbIFlfbZKCUnJE87m9Rl0SoSGihw'
        gmaps = Client(api_key)
        data = distance_matrix(gmaps, first_location, second_location)
        distance = data['rows'][0]['elements'][0]['distance']['text']
        self.ui.labelResult.setText('Distance between {} and {} is {}'.format(first_location, second_location, distance))


if __name__ == '__main__':
    app = QApplication(argv)
    window = MyForm()
    window.show()
    exit(app.exec_())
