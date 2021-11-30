:author:    D E Haynes
:made_at:   2021-11-30
:project:   Pity of Thieves

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Motivation.player

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Introduction
============

Open
----

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 0

There is a thud. From above.

|PLAYER_NAME| sits up in bed. She listens for a moment, confused.

Then looks toward the door.

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: DRAMA.state 1

Listen
------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 1

{0}

|PLAYER_NAME| listens for a moment.
She's not alone in the house. Is there going to be a problem?

.. property:: DRAMA.prompt Type a command to continue.
.. property:: DRAMA.state 0

.. |NPC_NAME| property:: NPC.name
.. |PLAYER_NAME| property:: PLAYER.name
