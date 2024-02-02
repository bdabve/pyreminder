#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : entry_2_modal.py
|      CREATED : 24-April-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : make form dialog modal, must fetch before destroy with entries
|        USAGE : ./entry_2_modal.py
\ ====================================================================================================
"""

from tkinter import *
from entry_2 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries)                  # must fetch before widow destroyed!
    popup.destroy()                 # fails with msgs if stmt order is reversed


def ask():
    popup = Toplevel()                      # show form in modal dialog window
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()             # wait for destroy here


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
