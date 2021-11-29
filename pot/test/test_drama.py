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

from balladeer import Stateful

from pot.drama import Drama
from pot.world import World


class DramaTests(unittest.TestCase):

    def setUp(self):
        self.drama = Drama("pot.interior", World())

    def test_spots(self):
        print(self.drama.folder)
        self.assertEqual(19, len(self.drama.folder), self.drama.folder)
