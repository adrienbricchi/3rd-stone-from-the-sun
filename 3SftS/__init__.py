#!/usr/bin/python3
# -*-coding:utf8 -*

#  3rd Stone from the Sun
#  Copyright (C) 2022
#  -
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  -
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  -
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.


import tkinter

import sv_ttk

from tkinter import ttk


window = tkinter.Tk()
window.title("sub-title-auto-correct")
window.geometry('1280x720')

fix_i_button = tkinter.Button(window, text="Hello")
fix_i_button.pack()

ttk.Label(window, text="Enter your comment :", font=("Times New Roman", 15))
text_field = tkinter.Text(window, width=20, height=3)
text_field.pack()

mb = tkinter.Menubutton(window, text="CheckComboBox")
mb.pack()
mb.menu = tkinter.Menu(mb, tearoff=0)
mb["menu"] = mb.menu

#imgvar2 = PhotoImage(file='timeline_logowhite_400.png')
mb.menu.add_command(label="Item0")
mb.menu.add_command(label="Item1")
mb.menu.add_command(label="Item2")

# This is where the magic happens
sv_ttk.set_theme("dark")

window.mainloop()
