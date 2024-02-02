#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : buttons3.py
|      CREATED : 06-Apr-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : adding buttons to widget and a user definded callback as a class
|        USAGE : ./buttons3.py
\ ====================================================================================================
"""
from tkinter import *


class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodby world..')                     # self.quit is a bound method
        self.quit()                                 # retains the self+quit pair


if __name__ == '__main__':
    HelloButton(text='Hello subclass world').mainloop()
    # widget = Button(None, text='Hello event world', command=HelloCallback())
    # widget.pack()
    # widget.mainloop()
