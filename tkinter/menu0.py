#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Tk8.0 style top-level window menus

import tkinter as tk                        # get widget classes
import tkinter.messagebox as tkmsg          # get standard dialogs


"""
Separator lines:
    The script makes a separator in the Edit menu with add_separator. it's just a line used to set off groups of related entries

Tear-offs:
    - The script also disables menu tear-offs in the Edit pull down by passing a tearoff=False widget option to Menu .
    - Tear-offs are dashed lines that appear by default at the top of tkinter menus and create a new window containing the menu’s contents when clicked.
    - They can be a convenient shortcut device (you can click items in the tear-off window right away, without having to navigate through menu trees), but they are not widely used on all platforms.

Keyboard shortcuts
    - The script uses the underline option to make a unique letter in a menu entry a keyboard shortcut.
    - It gives the offset of the shortcut letter in the entry’s label string.
"""


def notdone():
    tkmsg.showerror('Not implemented', 'Not yet available')


def makemenu(win):
    top = tk.Menu(win)                  # win=top-level window, atache Menu to window
    win.config(menu=top)                # set its menu option, cross-link window to menu

    mfile = tk.Menu(top)                                                        # attach a Menu to top Menu
    mfile.add_command(label='New...', command=notdone, underline=0)
    mfile.add_command(label='Open...', command=notdone, underline=0)
    mfile.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=mfile)                                   # cross-link parent to child

    edit = tk.Menu(top, tearoff=False)
    # Tearoff are dashed lines that appear by default at the top of tkinter menus

    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = tk.Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)


if __name__ == '__main__':
    root = tk.Tk()                 # or Toplevel()
    root.title('menu_win')      # set window-mgr info

    makemenu(root)              # associate a menu bar
    msg = tk.Label(root, text='Window menu basics')    # add something below
    msg.pack(expand='yes', fill='both')
    msg.config(relief='sunken', width=40, height=7, bg='beige')

    root.mainloop()
