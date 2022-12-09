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

import configparser
import json
import os

from jsonpath_ng import parse
from .Brand import *


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

OPEN_MIDI_ROOT_LOCATION = config["PARAMETERS"]['openmidi_root_location']
OPEN_MIDI_MAPPING_JSON = OPEN_MIDI_ROOT_LOCATION + "/data/mapping.json"


class OpenMidiParser:

    def __init__(self):
        """Prepare the OpenMidi data set"""
        self._mapping = self.__load_mapping_file()
        self._brands = self.__parse_brands()

    @staticmethod
    def __load_mapping_file():
        """Load the inner mapping.json file."""
        print(OPEN_MIDI_MAPPING_JSON)
        print(os.path.isfile(OPEN_MIDI_MAPPING_JSON))  # TODO : crash if not exist
        with open(OPEN_MIDI_MAPPING_JSON, 'r') as mapping_json_file:
            return json.load(mapping_json_file)

    def __parse_brands(self):
        """Parse some data in the inner mapping.json file."""
        jsonpath_expression = parse("$.brands[*]")
        raw_results = jsonpath_expression.find(self._mapping)
        parsed_objects = list(map(lambda result: result.value, raw_results))
        return list(map(lambda parsed_object: Brand(parsed_object["value"], parsed_object["name"]), parsed_objects))

    @property
    def brands(self):
        """Get the brands list."""
        return self._brands
