#!/usr/bin/env python3
# encoding: utf-8

# This is a parser-based text adventure.
# Copyright (C) 2021 D E Haynes

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
Usage:

~/py3.9-dev/bin/python -m ops.location_template >> pot/odric/13_exploration.rst

"""
from pot.world import Location

template = """
Play
----

{0}

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1
"""

for i in list(Location):
    print(i)
