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

|PLAYER_NAME| sits up in bed. He listens for a moment, confused.

Then looks toward the door.

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: DRAMA.state 1

Listen
------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 1

{0}

|PLAYER_NAME| listens for a moment.
He's not alone in the hut. Is there going to be a problem?

{exits}

.. property:: DRAMA.prompt Type a command to continue.
.. property:: DRAMA.state 0

Play
----

{0}

|PLAYER_LOCN|.

{exits}

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: DRAMA.state 1

.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.name
