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
from tkinter import Frame


brand_names = ["BOSS", "Digitech", "Strymon", "TC Electronic"]
pedal_names = ["BigSky", "Ditto x4", "EQ-200", "ML5", "Mobius", "Timeline", "Whammy"]


class BrandHeader:

    def __init__(self, window):
        self._view = tkinter.Menubutton(window, text="Brand")
        self._view.menu = tkinter.Menu(self._view, tearoff=0)
        self._view["menu"] = self._view.menu
        for brand_name in brand_names:
            # imgvar2 = PhotoImage(file='timeline_logowhite_400.png')
            self._view.menu.add_command(label=brand_name, image="")

    @property
    def view(self):
        """Get the populated view."""
        return self._view


class PedalHeader:

    def __init__(self, window):
        self._view = tkinter.Menubutton(window, text="Pedal")
        self._view.menu = tkinter.Menu(self._view, tearoff=0)
        self._view["menu"] = self._view.menu
        for pedal_name in pedal_names:
            # imgvar2 = PhotoImage(file='timeline_logowhite_400.png')
            self._view.menu.add_command(label=pedal_name, image="")

    @property
    def view(self):
        """Get the populated view."""
        return self._view


class MainWindow:

    def __init__(self):
        self._window = tkinter.Tk()
        self._window.title("3rd Stone from the Sun")
        self._window.geometry('1280x720')
        self.init_headers()

    @property
    def window(self):
        """Get the main window."""
        return self._window

    def init_headers(self):
        for i in range(1, 9):
            brand_header = BrandHeader(self._window)
            brand_header.view.grid(row=0, column=i)
            pedal_header = PedalHeader(self._window)
            pedal_header.view.grid(row=1, column=i)
