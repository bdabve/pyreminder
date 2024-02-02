import tkinter as tk

root = tk.Tk()

labelFont = ('times', 20, 'bold')
"""
Label’s font attribute take three-item tuple giving the
   * font family
   * size
   * style : can be normal, bold, roman, italic, underline, over strike, or combinations of these (e.g., “bold italic”).
"""
widget = tk.Label(root, text='Hello config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelFont)
widget.config(height=3, width=20)
widget.pack(expand='yes', fill='both')

btn = tk.Button(text='Click', padx=10, pady=10)

btn.pack(padx=20, pady=20)

btn.config(cursor='gumby')
btn.config(bd=8, relief='raised')
btn.config(bg='dark green', fg='white')
btn.config(font=('Monaco', 13, 'bold italic'))

root.mainloop()

"""
* Border and relief:
    - bd=N widget option can be used to set border width. and a
    - relief={FLAT, SUNKEN, RAISED, GROOVE, SOLID, or RIDGE—all} option can specify a border style

* Cursor
    - A cursor option can be given to change the appearance of the mouse pointer when
      it moves over the widget. like { watch, pencil, cross, hand2 }.

* State
    - Some widgets also support the notion of a state, which impacts their appearance, For example: state=DISABLED|NORMAL|READONLY.

* Padding
    - Extra space can be added around many widgets (e.g., buttons, labels, and text) with the padx=N and pady=N options.
"""
