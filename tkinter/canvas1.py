#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
/ ====================================================================================================
|
|         FILE :
|      CREATED :
|       AUTHOR : daBve, dabve@outlook.fr
|
|         DESC : demo all basic canvas interfaces
|        USAGE :
\ ====================================================================================================
"""

import tkinter as tk

canvas = tk.Canvas(width=525, height=300, bg='white')           # 0,0 is top left corner
"""
Canvases define an (X,Y) coordinate system for their drawing area; x means the horizontal scale, y means vertical.
By default, coordinates are measured in screen pixels (dots), the upper-left corner of the canvas has coordinates (0,0),
and x and y coordinates increase to the right and down, respectively.
"""
canvas.pack(expand='yes', fill='both')                          # increases down, right

canvas.create_line(100, 100, 200, 200)                          # fromX, fromY, toX, toY
canvas.create_line(100, 200, 200, 300)
"""
This script demonstrates all the basic graphic object constructor calls;
to each, you pass one or more sets of (X,Y) coordinates to give the new object’s location,
start point and endpoint, or diagonally opposite corners of a bounding box that encloses the shape:
    id = canvas.create_line(fromX, fromY, toX, toY) # line start, stop
    id = canvas.create_oval(fromX, fromY, toX, toY) # two opposite box corners
    id = canvas.create_arc( fromX, fromY, toX, toY) # two opposite oval corners
    id = canvas.create_rectangle(fromX, fromY, toX, toY) # two opposite corners
"""

for i in range(1, 20, 2):
    canvas.create_line(0, i, 50, i)

"""
The canvas allows you to draw and display common shapes such as lines, ovals, rectangles, arcs, and polygons.
In addition, you can embed text, images, and other kinds of tkinter widgets such as labels and buttons.
"""
canvas.create_oval(10, 10, 200, 200, width=2, fill='blue')
canvas.create_arc(200, 200, 300, 100)
canvas.create_rectangle(200, 200, 300, 300, width=5, fill='red')
canvas.create_line(0, 300, 150, 150, width=10, fill='green')

photo = tk.PhotoImage(file='..\\..\\bin\weather_configFiles\\landscape-1844227_960_720.png')
"""
Other drawing calls specify just one (X,Y) pair, to give the location of the object’s upperleft corner:
"""
canvas.create_image(325, 25, image=photo, anchor='nw')      # embed a photo

widget = tk.Label(canvas, text='Spam', fg='white', bg='black')
widget.pack()
canvas.create_window(100, 100, window=widget)               # embed a widget
canvas.create_text(100, 280, text='Ham')                    # draw some text

canvas.mainloop()
