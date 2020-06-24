#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:21:48 2020

@author: cathyli
"""


import tkinter
import random

# create event handler function when any key is hit on the canvas
def handle_key(event):
    if event.char == 'w':
        player1.move("u")
    if event.char == 's':
        player1.move("d")
    if event.char == 'a':
        player1.move("l")
    if event.char == 'd':
        player1.move("r")
    if event.char == 'i':
        player2.move("u")
    if event.char == 'k':
        player2.move("d")
    if event.char == 'j':
        player2.move("l")
    if event.char == 'l':
        player2.move("r")
        
    yellow_xy = canvas.bbox(1)
    overlapping = canvas.find_overlapping(
        yellow_xy[0],
        yellow_xy[1],
        yellow_xy[2],
        yellow_xy[3])
    if 2 in overlapping:
        canvas.create_text(100,
                           100,
                           font=('Arial',20),
                           text = 'Tag!',
                           tag = "tag_label")
    elif 2 not in overlapping:
        canvas.delete("tag_label")
        

# create class for player with randomly sized pieces
class Player(object):
    def __init__(self, canvas, color):
        self.color = color
        size = random.randint(1,100)
        x1 = random.randint(100,700)
        y1 = random.randint(100,700)
        x2 = x1+size
        y2 = y1+size
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_rectangle(self.coords)
        canvas.itemconfig(self.piece, fill=color)
    
    def move(self, direction):
        if direction == 'u':
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'd':
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == 'l':
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'r':
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)

# initialize window and widgets
window = tkinter.Tk()
window.geometry("800x800")
window.title("Tag!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')

player1 = Player(canvas, "purple")
player2 = Player(canvas, "orange")
canvas.bind_all('<Key>', handle_key)

window.mainloop()