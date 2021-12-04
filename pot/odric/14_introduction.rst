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
            pot.world.Spot.woodshed

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
.. condition:: LOCAL.state 0

Have you ever heard the sound of Rooks in early dawn?
The devilish cackle of hundreds of birds - they should call them a Mockery.
Harsh critics of anyone still in their bed.

So wakes |PLAYER_NAME|.

His place is the |PLAYER_SPOT|. Where he sleeps, and when sleep leaves him, where he must work.

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: LOCAL.state 1

Listen
------

.. condition:: PLAYER.state pot.world.Spot.woodshed
.. condition:: LOCAL.state 1

{0}

|PLAYER_NAME| climbs to his feet and sniffs the stale air of the  |PLAYER_SPOT|.

|PLAYER_NAME| listens for a moment. The Rooks are settling down again. There's no other sound to be heard.

{exits}

.. property:: DRAMA.prompt Type a command to continue.
.. property:: LOCAL.state 2

Bored
-----

.. condition:: PLAYER.state pot.world.Spot.woodshed
.. condition:: LOCAL.state 2

|PLAYER_NAME| isn't doing anything. He looks toward the door.

{exits}

.. property:: LOCAL.state 1

Exit
----

.. condition:: PLAYER.state pot.world.Spot.butchers_row

{0}

|PLAYER_NAME| steps out and breathes the early mist of the new day.

.. property:: LOCAL.state 0
.. property:: RAT.state pot.types.Engagement.acting
.. property:: POISON.state pot.types.Engagement.placed
.. property:: DRAMA.prompt Type a command or press Return to wait

.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_SPOT| property:: PLAYER.spot.title
.. |SPOT_NAME| property:: PLAYER.spot.name
