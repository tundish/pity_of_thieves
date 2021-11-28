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


from balladeer import Grouping
from balladeer.cartography import Compass
from balladeer.cartography import Map as MapType
from balladeer.cartography import Transit
from balladeer.cartography import Waypoint
from balladeer.world import World as WorldType


class Map(MapType):

    spots = {
        "beggars_ash":  ["beggar's ash", "beggars ash"],
        "cutthroat_lane":  ["cut throat lane", "cutthroat lane"],
        "dingwood":  ["dingwood"],
        "gardens":  ["public gardens", "gardens"],
        "mordiford_quay":  ["mordiford quay", "quay"],
        "tower_street_e":  ["upper tower street", "tower st e"],
        "tower_street":  ["tower street", "tower st"],
        "tower_street_w":  ["lower tower street", "tower st w"],
        "woodshed":  ["wood shed", "woodshed", "shed"],
    }

    Arriving = enum.Enum("Arriving", spots, type=Waypoint)
    Departed = enum.Enum("Departed", spots, type=Waypoint)
    Location = enum.Enum("Location", spots, type=Waypoint)

    def __init__(self, exit=None, into=None, **kwargs):
        super().__init__(exit, into, **kwargs)
        exit, into = self.exit, self.into

        self.transits = [
            Transit(label="shed door").set_state(exit.tower_st_w, Compass.S, into.woodshed, Via.bidir),
        ]


class World(WorldType):
    pass


Arriving = Map.Arriving
Departed = Map.Departed
Location = Map.Location
