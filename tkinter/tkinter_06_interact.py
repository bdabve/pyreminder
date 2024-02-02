#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : tkinter_06_interact.py
|      CREATED : 04-Apr-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : getting user input
|        USAGE : ./tkinter_06_interact.py
\ ====================================================================================================
"""

import tkinter
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='Hello {}!'.format(name))


"""
Three widgets attached to the Tk main top-level window
"""
top = tkinter.Tk()                              # The main window
top.title('Echo')                               # title of the window
# top.iconbitmap('py-blue-trans-out.ico')
tkinter.Label(top, text='Enter you name: ').pack(side='top')    # label for the entry
ent = tkinter.Entry(top)                                        # add entry like forms in webdev
ent.pack(side='top')
btn = tkinter.Button(top, text='Submit', command=(lambda: reply(ent.get())))        # add a button with command reply
btn.pack(side='left')

top.mainloop()
