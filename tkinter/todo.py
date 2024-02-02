#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : todo.py
|      CREATED : 06-August-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : A simple todo script with tkinter
|        USAGE : ./todo.py
 ====================================================================================================
"""

from tkinter import *


class MainFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)            # do superclass init
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        Label(self, text='Todo list').pack(side=TOP, fill=X)
        widget = Button(self, text='New', command=self.new_entry)
        widget.pack(side=LEFT)

    def new_entry(self):
        row = Frame(self)
        ent = Entry(row)

        row.pack(side=BOTTOM)
        ent.pack(side=TOP, fill=X)
        submit = Button(self, 'Submit', command=lambda: self.fetch(ent))
        submit.pack(side=RIGHT)

    def fetch(self, ent):
        print(ent.get())


if __name__ == '__main__':
    MainFrame().mainloop()
