:author:    D E Haynes
:made_at:   2021-12-07
:project:   The Pity of Thieves
:dwell: 0.2
:pause: 0.9

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Engagement.player

.. entity:: NPC
   :types:  pot.world.Character
   :states: pot.types.Proximity.present

.. entity:: LOCAL
   :types:  pot.world.Location

.. entity:: ITEM
   :types:  pot.world.Item
   :states: pot.types.Engagement.static

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.prompt

.. entity:: SETTINGS
   :types:  balladeer.Settings

Introduction
============

First impression
----------------

.. condition:: NPC.state 0

|NPC_NAME| is here.

.. property:: NPC.state 1
.. property:: NPC.state pot.types.Engagement.static
.. property:: DRAMA.prompt Press Return to talk with |NPC_NAME|

Second look
-----------

.. condition:: NPC.state 1

|NPC_NAME| is here.

.. property:: NPC.state 2
.. property:: DRAMA.prompt Type a command to continue.

Give
----

.. condition:: ITEM.holder.name |NPC_NAME|

|NPC_NAME| gives |PLAYER_NAME| the |ITEM_NAME|.

.. property:: ITEM.holder PLAYER

Gave
----

.. condition:: ITEM.holder.name |PLAYER_NAME|

|PLAYER_NAME| has the |ITEM_NAME|.

.. property:: ITEM.holder PLAYER
.. property:: NPC.state pot.types.Engagement.acting

.. |PLAYER_NAME| property:: PLAYER.name
.. |NPC_NAME| property:: NPC.name
.. |ITEM_NAME| property:: ITEM.names[0].noun
