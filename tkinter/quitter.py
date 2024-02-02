#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : dlg_quitter.py
|      CREATED : 22-Apr-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : a Quit button that verifies exit requests.
|                to reuse, attach an instance to other GUIs, and re-pack as desired
|        USAGE : ./dlg_quitter.py
\ ====================================================================================================
"""
from tkinter import *                               # get widget classes
from tkinter.messagebox import askokcancel          # get canned std dialog


class Quitter(Frame):                           # subclass our Gui
    def __init__(self, parent=None):            # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', comman=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')
        if ans: Frame.quit(self)


if __name__ == '__main__':
    Quitter().mainloop()
