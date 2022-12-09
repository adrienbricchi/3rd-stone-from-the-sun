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
from .OpenMidiParser import OpenMidiParser

open_midi = OpenMidiParser()
brands = open_midi.brands
pedal_names = ["BigSky", "Ditto x4", "EQ-200", "ML5", "Mobius", "Timeline", "Whammy"]


class BrandHeader:

    def __init__(self, window):
        """Build the composite view"""
        wrapper_frame = tkinter.Frame(window, width=100, height=25)
        wrapper_frame.columnconfigure(0, weight=10)
        wrapper_frame.grid_propagate(False)
        # Menu button
        menu_button = tkinter.Menubutton(wrapper_frame, text="Brand")
        menu_button.menu = tkinter.Menu(menu_button, tearoff=0)
        menu_button["menu"] = menu_button.menu
        for brand in brands:
            # imgvar2 = PhotoImage(file='timeline_logowhite_400.png')
            menu_button.menu.add_command(label=brand.name, image="")
        menu_button.grid(sticky="nesw")
        # Pack everything up
        self._view = wrapper_frame

    @property
    def view(self):
        """Get the populated view."""
        return self._view


class PedalHeader:

    def __init__(self, window):
        """Build the composite view"""
        wrapper_frame = tkinter.Frame(window, width=200, height=50)
        wrapper_frame.columnconfigure(0, weight=10)
        wrapper_frame.grid_propagate(False)
        # Menu button
        menu_button = tkinter.Menubutton(wrapper_frame, text="Pedal")
        menu_button.menu = tkinter.Menu(menu_button, tearoff=0)
        menu_button["menu"] = menu_button.menu
        for pedal_name in pedal_names:
            # imgvar2 = PhotoImage(file='timeline_logowhite_400.png')
            menu_button.menu.add_command(label=pedal_name, image="")
        menu_button.grid(sticky="nesw")
        # Pack everything up
        self._view = wrapper_frame

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
