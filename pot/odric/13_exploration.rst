:author:    D E Haynes
:made_at:   2021-11-30
:project:   The Pity of Thieves
:dwell: 0.2
:pause: 0.9

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Engagement.player

.. entity:: RAT
   :types:  pot.world.Character
   :states: pot.types.Engagement.acting
            pot.world.Location.woodshed

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Exploration
===========

beggars_ash_0
-------------

.. condition:: PLAYER.state pot.world.Location.beggars_ash
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

beggars_ash_1
-------------

.. condition:: PLAYER.state pot.world.Location.beggars_ash
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

beggars_ash_2
-------------

.. condition:: PLAYER.state pot.world.Location.beggars_ash
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

bridge_street_0
---------------

.. condition:: PLAYER.state pot.world.Location.bridge_street
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

bridge_street_1
---------------

.. condition:: PLAYER.state pot.world.Location.bridge_street
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

bridge_street_2
---------------

.. condition:: PLAYER.state pot.world.Location.bridge_street
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

butchers_row_0
--------------

.. condition:: PLAYER.state pot.world.Location.butchers_row
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

butchers_row_1
--------------

.. condition:: PLAYER.state pot.world.Location.butchers_row
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

butchers_row_2
--------------

.. condition:: PLAYER.state pot.world.Location.butchers_row
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

cutthroat_lane_0
----------------

.. condition:: PLAYER.state pot.world.Location.cutthroat_lane
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

cutthroat_lane_1
----------------

.. condition:: PLAYER.state pot.world.Location.cutthroat_lane
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

cutthroat_lane_2
----------------

.. condition:: PLAYER.state pot.world.Location.cutthroat_lane
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

dingwood_0
----------

.. condition:: PLAYER.state pot.world.Location.dingwood
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

dingwood_1
----------

.. condition:: PLAYER.state pot.world.Location.dingwood
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

dingwood_2
----------

.. condition:: PLAYER.state pot.world.Location.dingwood
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

gardens_0
---------

.. condition:: PLAYER.state pot.world.Location.gardens
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

gardens_1
---------

.. condition:: PLAYER.state pot.world.Location.gardens
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

gardens_2
---------

.. condition:: PLAYER.state pot.world.Location.gardens
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

market_0
--------

.. condition:: PLAYER.state pot.world.Location.market
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

market_1
--------

.. condition:: PLAYER.state pot.world.Location.market
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

market_2
--------

.. condition:: PLAYER.state pot.world.Location.market
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

market_house_0
--------------

.. condition:: PLAYER.state pot.world.Location.market_house
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

market_house_1
--------------

.. condition:: PLAYER.state pot.world.Location.market_house
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

market_house_2
--------------

.. condition:: PLAYER.state pot.world.Location.market_house
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

mordiford_quay_0
----------------

.. condition:: PLAYER.state pot.world.Location.mordiford_quay
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

mordiford_quay_1
----------------

.. condition:: PLAYER.state pot.world.Location.mordiford_quay
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

mordiford_quay_2
----------------

.. condition:: PLAYER.state pot.world.Location.mordiford_quay
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

north_gate_0
------------

.. condition:: PLAYER.state pot.world.Location.north_gate
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

north_gate_1
------------

.. condition:: PLAYER.state pot.world.Location.north_gate
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

north_gate_2
------------

.. condition:: PLAYER.state pot.world.Location.north_gate
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

orchard_0
---------

.. condition:: PLAYER.state pot.world.Location.orchard
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

orchard_1
---------

.. condition:: PLAYER.state pot.world.Location.orchard
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

orchard_2
---------

.. condition:: PLAYER.state pot.world.Location.orchard
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

ross_road_0
-----------

.. condition:: PLAYER.state pot.world.Location.ross_road
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

ross_road_1
-----------

.. condition:: PLAYER.state pot.world.Location.ross_road
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

ross_road_2
-----------

.. condition:: PLAYER.state pot.world.Location.ross_road
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

south_end_0
-----------

.. condition:: PLAYER.state pot.world.Location.south_end
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

south_end_1
-----------

.. condition:: PLAYER.state pot.world.Location.south_end
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

south_end_2
-----------

.. condition:: PLAYER.state pot.world.Location.south_end
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tavern_0
--------

.. condition:: PLAYER.state pot.world.Location.tavern
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tavern_1
--------

.. condition:: PLAYER.state pot.world.Location.tavern
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

tavern_2
--------

.. condition:: PLAYER.state pot.world.Location.tavern
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

top_cross_0
-----------

.. condition:: PLAYER.state pot.world.Location.top_cross
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

top_cross_1
-----------

.. condition:: PLAYER.state pot.world.Location.top_cross
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

top_cross_2
-----------

.. condition:: PLAYER.state pot.world.Location.top_cross
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_e_0
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_e
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_e_1
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_e
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

tower_street_e_2
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_e
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_0
--------------

.. condition:: PLAYER.state pot.world.Location.tower_street
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_1
--------------

.. condition:: PLAYER.state pot.world.Location.tower_street
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

tower_street_2
--------------

.. condition:: PLAYER.state pot.world.Location.tower_street
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_w_0
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_w
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_street_w_1
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_w
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

tower_street_w_2
----------------

.. condition:: PLAYER.state pot.world.Location.tower_street_w
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_wall_0
------------

.. condition:: PLAYER.state pot.world.Location.tower_wall
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

tower_wall_1
------------

.. condition:: PLAYER.state pot.world.Location.tower_wall
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

tower_wall_2
------------

.. condition:: PLAYER.state pot.world.Location.tower_wall
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

woodshed_0
----------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 0

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

woodshed_1
----------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 1

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 2

woodshed_2
----------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 2

{0}

.. todo

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1

Hurry
-----

.. condition:: PLAYER.in_transit True

{0}

|PLAYER_NAME| hurries past |PLAYER_LOCN|.

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

Fallback
--------

{0}

|PLAYER_LOCN|.

{exits}

.. fx:: pot.img |LOCN_NAME|.png
   :offset: 1
   :duration: 3

.. property:: DRAMA.state 1


.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.title
.. |LOCN_NAME| property:: PLAYER.location.name
