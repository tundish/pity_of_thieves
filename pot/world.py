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

import enum

from balladeer import Grouping
from balladeer import Stateful
from balladeer import Named
from balladeer import World as WorldType
from balladeer.cartography import Compass
from balladeer.cartography import Map as MapType
from balladeer.cartography import Transit as TransitType
from balladeer.cartography import Via
from balladeer.cartography import Waypoint
from balladeer.speech import Article
from balladeer.speech import Name
from balladeer.speech import Pronoun

from pot.types import Engagement
from pot.types import Operation


class Transit(Named, TransitType): pass


class Map(MapType):

    spots = {
        "beggars_ash":  ["beggar's ash", "beggars ash"],
        "bridge_street":  ["bridge street", "bridge st"],
        "butchers_row":  ["butchers' row", "butchers row"],
        "cutthroat_lane":  ["cut throat lane", "cutthroat lane"],
        "dingwood":  ["dingwood"],
        "gardens":  ["public gardens", "gardens"],
        "market":  ["market"],
        "market_house":  ["market house"],
        "mordiford_quay":  ["mordiford quay", "quay"],
        "north_gate":  ["north gate", "northgate"],
        "orchard":  ["the orchard", "orchard"],
        "ross_road":  ["ross road", "ross rd"],
        "south_end":  ["south end", "southend"],
        "tavern":  ["tavern"],
        "top_cross":  ["top cross"],
        "tower_street_e":  ["upper tower street", "tower st e"],
        "tower_street":  ["tower street", "tower st"],
        "tower_street_w":  ["lower tower street", "tower st w"],
        "tower_wall":  ["tower wall"],
        "woodshed":  ["wood shed", "woodshed", "shed"],
        "inventory": []
    }

    Arriving = enum.Enum("Arriving", spots, type=Waypoint)
    Departed = enum.Enum("Departed", spots, type=Waypoint)
    Location = enum.Enum("Location", spots, type=Waypoint)

    def __init__(self, exit=None, into=None, **kwargs):
        super().__init__(exit, into, **kwargs)
        exit, into = self.exit, self.into

        self.transits = [
            Transit().set_state(exit.north_gate, Compass.E, into.beggars_ash, Via.bidir),
            Transit().set_state(exit.north_gate, Compass.W, into.orchard, Via.bidir),
            Transit(
                names=[Name("Shed door"), Name("Door")]
            ).set_state(exit.butchers_row, Compass.E, into.woodshed, Via.bidir),
            Transit().set_state(exit.butchers_row, Compass.N, into.north_gate, Via.bidir),
            Transit().set_state(exit.butchers_row, Compass.SE, into.market, Via.bidir),
            Transit().set_state(exit.butchers_row, Compass.S, into.top_cross, Via.bidir),
            Transit().set_state(exit.butchers_row, Compass.W, into.bridge_street, Via.bidir),
            Transit().set_state(exit.market, Compass.E, into.tower_street_w, Via.bidir),
            Transit().set_state(exit.market, Compass.S, into.market_house, Via.bidir),
            Transit().set_state(exit.top_cross, Compass.E, into.market_house, Via.bidir),
            Transit().set_state(exit.top_cross, Compass.S, into.south_end, Via.bidir),
            Transit().set_state(exit.top_cross, Compass.SW, into.ross_road, Via.bidir),
            Transit().set_state(exit.ross_road, Compass.SW, into.mordiford_quay, Via.bidir),
            Transit().set_state(exit.south_end, Compass.S, into.dingwood, Via.bidir),
            Transit().set_state(exit.tower_street_w, Compass.E, into.tower_street, Via.bidir),
            Transit().set_state(exit.tower_street, Compass.E, into.tower_street_e, Via.bidir),
            Transit(
                names=[Name("Oak door"), Name("Door")]
            ).set_state(exit.tower_street, Compass.N, into.tavern, Via.bidir),
            Transit().set_state(exit.tower_street_e, Compass.E, into.tower_wall, Via.bidir),
            Transit().set_state(exit.tower_street_e, Compass.N, into.gardens, Via.bidir),
            Transit().set_state(exit.gardens, Compass.NE, into.cutthroat_lane, Via.bidir),
            Transit(
                names=[Name("Muddy path"), Name("Path")]
            ).set_state(exit.cutthroat_lane, Compass.W, into.north_gate, Via.bidir),
        ]

Arriving = Map.Arriving
Departed = Map.Departed
Location = Map.Location


class Located(Stateful):

    @property
    def location(self):
        return self.get_state(Location)


class Mobile(Located):

    @property
    def in_transit(self):
        return (self.get_state(Arriving)
            and self.get_state(Arriving).name != self.get_state(Location).name
        )


class Character(Named, Mobile): pass
class Item(Named, Located): pass


class World(WorldType):

    def __init__(self, map_, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map = map_

    def build(self):
        return [
            Character(
                names=[Name("Odric", Article("", ""), Pronoun("he", "him", "himself", "his"))],
                description="{0.names[0].noun} is a scruffy little orphan."
            ).set_state(Engagement.player, Location.woodshed),
            Character(
                names=[Name("Niall", Article("", ""), Pronoun("he", "him", "himself", "his"))],
                description="{0.names[0].noun} is a fit young man with long hair and wild eyes."
            ).set_state(Engagement.acting, Location.top_cross),
            Character(
                names=[Name("Freda", Article("", ""), Pronoun("she", "her", "herself", "her"))],
                description="{0.names[0].noun} is a tall girl, graceful and fair."
            ).set_state(Engagement.acting, Location.tavern),
            Character(
                names=[Name("Isla", Article("", ""), Pronoun("she", "her", "herself", "her"))],
                description="{0.names[0].noun} is sharp and nimble. Because she's a Rat."
            ).set_state(Engagement.hidden, Location.woodshed),
            Character(
                names=[Name("Hod", Article("", ""), Pronoun("he", "him", "himself", "his"))],
                description="{0.names[0].noun} is sharp and nimble."
            ).set_state(Engagement.acting, Location.beggars_ash),
            Item(
                names=[Name("Arsenic"), Name("Poison"), Name("Granules")],
                description="A small waxed leather bag, full of crunchy white granules."
            ).set_state(Engagement.hidden, Location.woodshed),
            Item(
                names=[Name("Knife"), Name("Seax")],
                description="A hefty blade. A tool rather than a weapon; it has a plain wooden handle."
            ).set_state(Engagement.placed, Location.orchard),
            Item(
                names=[Name("Cheese"), Name("Food")],
                description="A chunk of hard {0.names[0].noun}, about the size of a fist."
            ).set_state(Engagement.placed, Location.tavern),
        ]


