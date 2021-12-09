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
   :states: pot.types.Engagement.acting
            pot.types.Proximity.present

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

Test
----

|NPC_NAME| gives |PLAYER_NAME| the |ITEM_NAME|.

.. property:: ITEM.holder PLAYER

.. |PLAYER_NAME| property:: PLAYER.name
.. |NPC_NAME| property:: NPC.name
.. |ITEM_NAME| property:: ITEM.names[0].noun
