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

import unittest

from balladeer import World
from balladeer.speech import Name

from turberfield.catchphrase.parser import CommandParser

from pot.drama import Drama
from pot.types import Motivation
from pot.world import Character
from pot.world import Location
from pot.world import Map
from pot.world import World


class DramaTests(unittest.TestCase):

    class TestWorld(World):

        def build(self):
            return [Character(names=[Name("test")]).set_state(Motivation.player, Location.woodshed)]

    def setUp(self):
        world = DramaTests.TestWorld(Map())
        self.drama = Drama("pot.interior", world)

    def test_spots(self):
        self.assertEqual(2, len(self.drama.folder), self.drama.folder)

    def test_if_mobile(self):
        player = next(iter(self.drama.ensemble))
        player.set_state(
            self.drama.world.map.Departed.mordiford_quay,
            self.drama.world.map.Location.mordiford_quay,
            self.drama.world.map.Arriving.cutthroat_lane,
        )
        Location = self.drama.world.map.Location
        for n in range(6):
            rv = next(self.drama.if_mobile(self.drama.ensemble), None)
            with self.subTest(n=n):
                if n == 4:
                    self.assertIs(player, rv)
                    self.assertEqual(
                        Location.cutthroat_lane,
                        player.get_state(Location)
                    )
                elif n == 5:
                    self.assertIsNone(rv)
                    self.assertEqual(
                        Location.cutthroat_lane,
                        player.get_state(Location)
                    )
                else:
                    self.assertIs(player, rv)
                    self.assertNotEqual(
                        Location.cutthroat_lane,
                        player.get_state(Location)
                    )

    def test_interlude(self):
        facts = self.drama.interlude(self.drama.folder, 0)
        self.assertIsInstance(facts, dict)
        self.assertIn("exits", facts)
        self.assertIn("**W**", facts["exits"], facts)
        self.assertIn("shed door", facts["exits"].lower(), facts)

    def test_hop(self):
        Arriving = self.drama.world.map.Arriving
        Location = self.drama.world.map.Location
        Departed = self.drama.world.map.Departed

        self.assertEqual(Location.woodshed, self.drama.player.get_state(Location))
        rv = CommandParser.expand_commands(self.drama.do_hop, ensemble=self.drama.ensemble, parent=self.drama)
        commands = {i[0] for i in rv}
        self.assertIn("n", commands)
        self.assertIn("go n", commands)
        self.assertIn("w", commands)
        self.assertIn("go w", commands)

        fn, args, kwargs = self.drama.interpret(self.drama.match("w"))
        self.assertEqual(self.drama.do_hop, fn)

        fn, args, kwargs =self.drama.interpret(self.drama.match("go w"))
        self.assertEqual(self.drama.do_hop, fn)

        response = self.drama(fn, *args, **kwargs)
        self.assertIn("W", response)
        self.assertEqual(Departed.woodshed, self.drama.player.get_state(Departed))
        self.assertEqual(Arriving.butchers_row, self.drama.player.get_state(Arriving))
