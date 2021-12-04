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
            pot.world.Spot.woodshed

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Exploration
===========

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

.. property:: DRAMA.state 1


.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_SPOT| property:: PLAYER.spot.title
.. |SPOT_NAME| property:: PLAYER.spot.name
