#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

master = Tk()

LabelFrame(master, text='Choose from the list').pack()

# w = Spinbox(master, from_=0, to=10)
w = Spinbox(master, values=('BHS', 'AUTOP', 'MOS'))
w.pack()
mainloop()
