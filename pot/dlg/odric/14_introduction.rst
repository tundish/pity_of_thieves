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
   :states: pot.types.Engagement.hidden
            pot.types.Proximity.present

.. entity:: POISON
   :types:  pot.world.Item
   :states: pot.types.Engagement.hidden
            pot.world.Spot.woodshed

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Introduction
============

Open
----

.. condition:: PLAYER.state pot.world.Spot.woodshed
.. condition:: DRAMA.state 0

Do you know the sound of Rooks at dawn?

Harsh critics of anyone still in their bed.

They should call that cackle a Mockery.

So wakes |PLAYER_NAME|.

He is in the |PLAYER_SPOT|. Where he sleeps, and when not sleeping, where he works.

.. property:: DRAMA.prompt Type 'look'. Or 'help' for other commands.
.. property:: DRAMA.state 1

Listen
------

.. condition:: PLAYER.state pot.world.Spot.woodshed
.. condition:: DRAMA.state 1

{0}

|PLAYER_NAME| listens for a moment. The Rooks are settling down again. There's no other sound to be heard.

{exits}

.. property:: DRAMA.prompt Type a command to continue.
.. property:: DRAMA.state 2

Bored
-----

.. condition:: PLAYER.state pot.world.Spot.woodshed
.. condition:: DRAMA.state 2

|PLAYER_NAME| isn't doing anything. He looks toward the door.

{exits}

.. property:: DRAMA.state 1

.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_SPOT| property:: PLAYER.spot.title
.. |SPOT_NAME| property:: PLAYER.spot.name
