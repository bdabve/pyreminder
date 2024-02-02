#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from quitter import Quitter


def fetch():
    print('Input => {}'.format(ent.get()))


root = Tk()
ent = Entry(root)
ent.insert(0, 'Type words here')    # set value like value in html tags
ent.pack(side=TOP, fill=X)          # grow horiz


ent.focus()                                         # save a click
ent.bind('<Return>', (lambda event: fetch()))       # on entry key
btn = Button(root, text='Fetch', command=fetch)  # and on button
btn.pack(side='left')
Quitter(root).pack(side='right')
root.mainloop()
