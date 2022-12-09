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


class Brand:

    def __init__(self, identifier, name):
        self._identifier = identifier
        self._name = name

    @property
    def identifier(self):
        """Get the id."""
        return self._identifier

    @property
    def name(self):
        """Get the name."""
        return self._name
