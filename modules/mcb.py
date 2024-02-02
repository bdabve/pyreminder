#! python3
# coding: utf-8
# -------------------------------------------------------------------
# mcb.pyw   : Saves and loads pieces of text to the clipboard.
#
# When you run py mcb.pyw save spam, the current contents of the clipboard will be saved with the keyword spam.
# This text can later be loaded to the clipboard again by running py mcb.pyw spam.
# And if the user forgets what keywords they have, they can run py mcb.pyw list to copy a list of all keywords to the clipboard.
#
# Usage     : py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#             py.exe mcb.pyw delete <keyword> - delete keyword from the shelf.
#             py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#             py.exe mcb.pyw list - Loads all keywords to clipboard.
# -------------------------------------------------------------------

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        # Delete keyword from the shelv
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
