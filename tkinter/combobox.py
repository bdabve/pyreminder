#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE :
|      CREATED :
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC :
|        USAGE :
\ ====================================================================================================
"""

from tkinter import *
from tkinter import ttk


def callback_function(event):
    print('New Item Selected: {}'.format(event.widget.get()))


app = Tk()
app.geometry('200x100')

label_top = Label(app, text='Choose you favourite month')
label_top.grid(column=0, row=0)

combo_box = ttk.Combobox(app, values=['January', 'February', 'March', 'April'])
combo_box.grid(column=0, row=1)
combo_box.current(1)
print(combo_box.current(), combo_box.get())
combo_box.bind('<<ComboboxSelected>>', lambda e: callback_function(e))

app.mainloop()
