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
import argparse
import sys

from pot.world import Location

template = """
.. condition:: PLAYER.state pot.world.{2}
.. condition:: DRAMA.state {0}

{{0}}

|PLAYER_LOCN|.

{{exits}}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state {1}
"""

p = argparse.ArgumentParser()
p.add_argument(
    "--repeat", type=int, default=3,
    help="Set the number of times to repeat a location section [3]"
)
p.add_argument(
    "--loop-to", type=int, default=1,
    help="Loop back to section number [1]"
)

args = p.parse_args()

l = 0
for i in list(Location):
    if not i.value:
        continue
    else:
        l += 1

    for n in range(args.repeat):
        name = f"{i.name}_{n}"
        print(name)
        print("-" * len(name))
        print(template.format(n, max((n + 1) % args.repeat, args.loop_to % args.repeat), i))

print("Wrote {0} sections.".format(args.repeat * l), file=sys.stderr)
