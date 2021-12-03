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

Hurry
-----

.. condition:: PLAYER.in_transit True

{0}

|PLAYER_NAME| hurries past |PLAYER_LOCN|.

Play
----

{0}

|PLAYER_LOCN|.

{exits}

.. property:: DRAMA.state 1


.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.title
