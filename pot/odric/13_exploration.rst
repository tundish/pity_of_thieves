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
.. |PLAYER_LOCN| property:: PLAYER.spot.title
.. |LOCN_NAME| property:: PLAYER.spot.name
