#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# use lambda as a callback function for buttons
from tkinter import *
import sys


def hello(event):
    print('Press twice to exit')            # on single-left click


def quit(event):                            # on double-left click
    print('Hello i must be going')          # event gives widget, x/y, etc.
    sys.exit()


root = Tk()
button = Button(root, text='Event Button with bind')
button.pack()
button.bind('<Button-1>', hello)             # bind left mouse clicks
button.bind('<Double-1>', quit)              # bind double-left clicks

widget = Button(root, text='Press to quit', command=(lambda: print('i will be going...') or sys.exit()))
# or operator in lambda to force two expressions to be run
widget.pack()
root.mainloop()
