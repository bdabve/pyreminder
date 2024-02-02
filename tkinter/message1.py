#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

"""
- The Message widget is simply a place to display text.
- Although the standar showinfo dialog is perhaps a better way to display pop-up messages.
- Message splits up long strings automatically and flexibly and can be embedded inside container widgets any time you need to add some read-only text to a display.
"""
msg = tk.Message(text='This is message a text message')

msg.config(bg='pink', font=('Monaco', 15, 'italic'))
msg.pack(fill='y', expand='yes')

msg.mainloop()
