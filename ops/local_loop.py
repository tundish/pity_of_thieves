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
Generates a number of shots which loop by storing state on the Location object.

Usage:

~/py3.9-dev/bin/python -m ops.local_loop >> pot/odric/13_exploration.rst

"""
import argparse
import sys

from pot.world import Spot

template = """
.. condition:: PLAYER.state pot.world.{0}
.. condition:: LOCAL.state {1}

{{0}}
{2}
|PLAYER_SPOT|.

{{exits}}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state {3}
"""

p = argparse.ArgumentParser()
p.add_argument(
    "--repeat", type=int, default=3,
    help="Set the number of times to repeat a spot section [3]"
)
p.add_argument(
    "--loop-to", type=int, default=1,
    help="Loop back to section number [1]"
)
p.add_argument(
    "--tag", action="store_true", default=False,
    help="Add text to display the section name [False]"
)
p.add_argument(
    "--todo", action="store_true", default=False,
    help="Add text to display a 'TODO' message [False]"
)

args = p.parse_args()

l = 0
for i in list(Spot):
    if not i.value:
        continue
    else:
        l += 1

    for n in range(args.repeat):
        name = f"{i.name}_{n}"
        print(name)
        print("-" * len(name))
        print(template.format(
            i,
            n,
            "\n.. todo\n" if args.todo else name if args.tag else "",
            max((n + 1) % args.repeat, args.loop_to % args.repeat),
        ))

print("Wrote {0} sections.".format(args.repeat * l), file=sys.stderr)
