:author:    D E Haynes
:made_at:   2021-11-30
:project:   The Pity of Thieves
:dwell: 0.2
:pause: 0.9

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Engagement.player

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


.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.title
