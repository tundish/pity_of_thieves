:author:    D E Haynes
:made_at:   2021-12-15
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

|PLAYER_NAME| hears a scratching sound.

High up in the rafters of |LOCN_ARTICLE| |LOCN_NAME|, there is movement.

He hops on to a log to get a better look. 
Two black eyes stare back.

The rat sits up straight, paws on her hips in an indignant fashion.

.. property:: NPC.state 1
.. property:: NPC.state pot.types.Engagement.static
.. property:: DRAMA.prompt Press Return to talk with |NPC_NAME|

Second look
-----------

.. condition:: NPC.state 1

[NPC]_

    |PLAYER_NAME|, would you mind getting rid of that please?

She nods over to the |ITEM_NAME|.

[NPC]_

    Life is hard enough already without people poisoning my kids.

.. property:: NPC.state 2
.. property:: DRAMA.prompt Type a command to continue.

Gave
----

.. condition:: ITEM.holder.name |PLAYER_NAME|

|ITEM_HOLDER| looks down at the |ITEM_NAME| he's holding.

.. todo Explain and activate travel

.. property:: ITEM.holder PLAYER
.. property:: NPC.state pot.types.Engagement.acting

.. |PLAYER_NAME| property:: PLAYER.name
.. |NPC_NAME| property:: NPC.name
.. |ITEM_NAME| property:: ITEM.names[0].noun
.. |ITEM_AKA| property:: ITEM.names[1].noun
.. |ITEM_HOLDER| property:: ITEM.holder.names[0].noun
.. |LOCN_NAME| property:: LOCAL.names[0].noun
.. |LOCN_ARTICLE| property:: LOCAL.names[0].article.definite
