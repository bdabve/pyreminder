#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE : entry_withLabels.py
|      CREATED : 22-Apr-2019
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC :
|        USAGE :
\ ====================================================================================================
"""
"""
use Entry widgets directly
lay out by rows with fixed-width labels: this and grid are best for forms
"""

import tkinter as tk
from dlg_quitter import Quitter

fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input => {}'.format(entry.get()))            # get text


def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)                        # make a new row
        lab = tk.Label(row, width=5, text=field)    # add label, entry
        ent = tk.Entry(row)
        row.pack(side='top', fill='x')
        lab.pack(side='left')
        ent.pack(side='right', expand='yes', fill='x')  # grow horizontal
        entries.append(ent)
    return entries


if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event: fetch(ents)))
    tk.Button(root, text='Fetch', command=(lambda: fetch(ents))).pack(side='left')
    Quitter(root).pack(side='right')
    root.mainloop()
