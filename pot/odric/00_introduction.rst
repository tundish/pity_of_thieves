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

Introduction
============

Open
----

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 0

Have you ever heard the sound of Rooks in early dawn?
The devilish cackle of hundreds of birds - they should call them a Mockery.
Harsh critics of anyone still in their bed.

So wakes |PLAYER_NAME|.

His place is the |PLAYER_LOCN|. Where he sleeps, and when sleep is gone, where he must work.

He looks toward the door.

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: DRAMA.state 1

Listen
------

.. condition:: PLAYER.state pot.world.Location.woodshed
.. condition:: DRAMA.state 1

{0}

|PLAYER_LOCN|.

|PLAYER_NAME| listens for a moment. Is there going to be a problem?

{exits}

.. property:: DRAMA.prompt Type a command to continue.

Play
----

{0}

|PLAYER_LOCN|.

{exits}

.. property:: DRAMA.prompt Type 'help'. Or 'again' to read once more.
.. property:: DRAMA.state 1

.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.title
