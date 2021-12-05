:author:    D E Haynes
:made_at:   2021-11-30
:project:   The Pity of Thieves
:dwell: 0.2
:pause: 0.9

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Engagement.player

.. entity:: LOCAL
   :types:  pot.world.Location

.. entity:: RAT
   :types:  pot.world.Character
   :states: pot.types.Engagement.acting
            pot.world.Spot.woodshed

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Exploration
===========

beggars_ash_0
-------------

.. condition:: LOCAL.state pot.world.Spot.beggars_ash
.. condition:: LOCAL.state 0

{0}

|PLAYER_SPOT| is a clearing by the road as it winds North.
A large dead tree, white and split open, gives this place a name.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

beggars_ash_1
-------------

.. condition:: LOCAL.state pot.world.Spot.beggars_ash
.. condition:: LOCAL.state 1

{0}

All there is at |PLAYER_SPOT| is a large dead tree, white and split open.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

beggars_ash_2
-------------

.. condition:: LOCAL.state pot.world.Spot.beggars_ash
.. condition:: LOCAL.state 2

{0}

There is nothing for |PLAYER_NAME| in |PLAYER_SPOT|. No need to go on further.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

bridge_street_0
---------------

.. condition:: LOCAL.state pot.world.Spot.bridge_street
.. condition:: LOCAL.state 0

{0}

Up to now, the path has been strewn with rushes to keep down the mud.
Here it is a wooden boardwalk, which becomes a bridge across the river.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

bridge_street_1
---------------

.. condition:: LOCAL.state pot.world.Spot.bridge_street
.. condition:: LOCAL.state 1

{0}

|PLAYER_SPOT| leads to a gate, and beyond that the bridge across the river.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

bridge_street_2
---------------

.. condition:: LOCAL.state pot.world.Spot.bridge_street
.. condition:: LOCAL.state 2

{0}

There is a gate at the end of |PLAYER_SPOT|, to hold the animals before they come to Market.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

butchers_row_0
--------------

.. condition:: LOCAL.state pot.world.Spot.butchers_row
.. condition:: LOCAL.state 0

{0}

No one yet is around at |PLAYER_SPOT|, although it can get busy.
The beasts which are not sold at Market end up here.

The whole place reeks of flesh. Even now in the wintry morning, there is a carnal stench
from every muddy puddle.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

butchers_row_1
--------------

.. condition:: LOCAL.state pot.world.Spot.butchers_row
.. condition:: LOCAL.state 1

{0}

In |PLAYER_SPOT|, long wooden trestles are set up either side of the street.
There are frames for hanging the meat, and big butts for blood and offal.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

butchers_row_2
--------------

.. condition:: LOCAL.state pot.world.Spot.butchers_row
.. condition:: LOCAL.state 2

{0}

The straw underfoot is filthy, bound with dung and blood.
|PLAYER_SPOT| is not a place to hang around.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

cutthroat_lane_0
----------------

.. condition:: LOCAL.state pot.world.Spot.cutthroat_lane
.. condition:: LOCAL.state 0

{0}

|PLAYER_NAME| takes a moment to stop and listen. There is a Woodpecker somewhere
above. His knocking echoes around the trees here on |PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

cutthroat_lane_1
----------------

.. condition:: LOCAL.state pot.world.Spot.cutthroat_lane
.. condition:: LOCAL.state 1

{0}

|PLAYER_SPOT| climbs and winds between ancient trees.
Here and there are pathways off to remote dwellings.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

cutthroat_lane_2
----------------

.. condition:: LOCAL.state pot.world.Spot.cutthroat_lane
.. condition:: LOCAL.state 2

{0}

|PLAYER_SPOT| is a little-used track which runs from the North Gate.
It can take you back into the village if you go far enough.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

dingwood_0
----------

.. condition:: LOCAL.state pot.world.Spot.dingwood
.. condition:: LOCAL.state 0

{0}

|PLAYER_NAME| rarely ventures down this way. It is the road
South, past |PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

dingwood_1
----------

.. condition:: LOCAL.state pot.world.Spot.dingwood
.. condition:: LOCAL.state 1

{0}

Further in this direction the road passes through the green hills of |PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

dingwood_2
----------

.. condition:: LOCAL.state pot.world.Spot.dingwood
.. condition:: LOCAL.state 2

{0}

Looking South. There is nothing beyond for miles.

|PLAYER_NAME| has gone to |PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

gardens_0
---------

.. condition:: LOCAL.state pot.world.Spot.gardens
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

gardens_1
---------

.. condition:: LOCAL.state pot.world.Spot.gardens
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

gardens_2
---------

.. condition:: LOCAL.state pot.world.Spot.gardens
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

market_0
--------

.. condition:: LOCAL.state pot.world.Spot.market
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

market_1
--------

.. condition:: LOCAL.state pot.world.Spot.market
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

market_2
--------

.. condition:: LOCAL.state pot.world.Spot.market
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

market_house_0
--------------

.. condition:: LOCAL.state pot.world.Spot.market_house
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

market_house_1
--------------

.. condition:: LOCAL.state pot.world.Spot.market_house
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

market_house_2
--------------

.. condition:: LOCAL.state pot.world.Spot.market_house
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

mordiford_quay_0
----------------

.. condition:: LOCAL.state pot.world.Spot.mordiford_quay
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

mordiford_quay_1
----------------

.. condition:: LOCAL.state pot.world.Spot.mordiford_quay
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

mordiford_quay_2
----------------

.. condition:: LOCAL.state pot.world.Spot.mordiford_quay
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

north_gate_0
------------

.. condition:: LOCAL.state pot.world.Spot.north_gate
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

north_gate_1
------------

.. condition:: LOCAL.state pot.world.Spot.north_gate
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

north_gate_2
------------

.. condition:: LOCAL.state pot.world.Spot.north_gate
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

orchard_0
---------

.. condition:: LOCAL.state pot.world.Spot.orchard
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

orchard_1
---------

.. condition:: LOCAL.state pot.world.Spot.orchard
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

orchard_2
---------

.. condition:: LOCAL.state pot.world.Spot.orchard
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

ross_road_0
-----------

.. condition:: LOCAL.state pot.world.Spot.ross_road
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

ross_road_1
-----------

.. condition:: LOCAL.state pot.world.Spot.ross_road
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

ross_road_2
-----------

.. condition:: LOCAL.state pot.world.Spot.ross_road
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

south_end_0
-----------

.. condition:: LOCAL.state pot.world.Spot.south_end
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

south_end_1
-----------

.. condition:: LOCAL.state pot.world.Spot.south_end
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

south_end_2
-----------

.. condition:: LOCAL.state pot.world.Spot.south_end
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tavern_0
--------

.. condition:: LOCAL.state pot.world.Spot.tavern
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tavern_1
--------

.. condition:: LOCAL.state pot.world.Spot.tavern
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

tavern_2
--------

.. condition:: LOCAL.state pot.world.Spot.tavern
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

top_cross_0
-----------

.. condition:: LOCAL.state pot.world.Spot.top_cross
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

top_cross_1
-----------

.. condition:: LOCAL.state pot.world.Spot.top_cross
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

top_cross_2
-----------

.. condition:: LOCAL.state pot.world.Spot.top_cross
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_e_0
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_e
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_e_1
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_e
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

tower_street_e_2
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_e
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_0
--------------

.. condition:: LOCAL.state pot.world.Spot.tower_street
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_1
--------------

.. condition:: LOCAL.state pot.world.Spot.tower_street
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

tower_street_2
--------------

.. condition:: LOCAL.state pot.world.Spot.tower_street
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_w_0
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_w
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_street_w_1
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_w
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

tower_street_w_2
----------------

.. condition:: LOCAL.state pot.world.Spot.tower_street_w
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_wall_0
------------

.. condition:: LOCAL.state pot.world.Spot.tower_wall
.. condition:: LOCAL.state 0

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

tower_wall_1
------------

.. condition:: LOCAL.state pot.world.Spot.tower_wall
.. condition:: LOCAL.state 1

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

tower_wall_2
------------

.. condition:: LOCAL.state pot.world.Spot.tower_wall
.. condition:: LOCAL.state 2

{0}

.. todo

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

yard_0
------

.. The best building logs are traditionally cut near a new moon in the Winter.

.. condition:: LOCAL.state pot.world.Spot.yard
.. condition:: LOCAL.state 0

{0}

The |PLAYER_SPOT| is damp and hung with mist. Stacks of
logs line the way out into the village.

It is Winter and the |PLAYER_SPOT| has been busy.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

yard_1
------

.. condition:: LOCAL.state pot.world.Spot.yard
.. condition:: LOCAL.state 1

{0}

In the |PLAYER_SPOT|.

The wood piles are neat and evenly spaced.
The largest logs over a foot in diameter.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

yard_2
------

.. condition:: LOCAL.state pot.world.Spot.yard
.. condition:: LOCAL.state 2

{0}

In the |PLAYER_SPOT|.

The green is kept separate from the dead.
All sorted according to bow, grain and taper.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

woodshed_0
----------

.. condition:: LOCAL.state pot.world.Spot.woodshed
.. condition:: LOCAL.state 0

{0}

The |PLAYER_SPOT| is stacked nearly full of logs and kindling.
It isn't easy to tell where the wood ends and the shed begins.

There is one space kept clear, and in it a wooden cot and a sort of shelf.

Around the floor are bits of debris; bark and rodent droppings.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

woodshed_1
----------

.. condition:: LOCAL.state pot.world.Spot.woodshed
.. condition:: LOCAL.state 1

{0}

The |PLAYER_SPOT| is stacked nearly full of logs and kindling.
The bundles of wood help to block the gaps in the wall panels.

|PLAYER_NAME| keeps a space clear for sleeping.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 2

woodshed_2
----------

.. condition:: LOCAL.state pot.world.Spot.woodshed
.. condition:: LOCAL.state 2

{0}

The |PLAYER_SPOT| is draughty but dry. There is thatch in the roof space.

Around the floor are bits of debris; bark and rodent droppings.


{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1

Hurry
-----

.. condition:: PLAYER.in_transit True

{0}

|PLAYER_NAME| hurries past |PLAYER_SPOT|.

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

Fallback
--------

{0}

|PLAYER_SPOT|.

{exits}

.. fx:: pot.img |SPOT_NAME|.png
   :offset: 1
   :duration: 3

.. property:: LOCAL.state 1


.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_SPOT| property:: PLAYER.spot.title
.. |SPOT_NAME| property:: PLAYER.spot.name
