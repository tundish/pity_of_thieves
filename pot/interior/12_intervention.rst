:author:    D E Haynes
:made_at:   2021-11-30
:project:   Pity of Thieves
:dwell:     0
:pause:     0

.. entity:: PLAYER
   :types:  pot.world.Character
   :states: pot.types.Motivation.player

.. entity:: DRAMA
   :types:  balladeer.Drama
   :states: pot.types.Operation.paused

.. entity:: SETTINGS
   :types:  balladeer.Settings


Intervention
============

Help
----

.. condition:: DRAMA.history[0].name do_help

[DRAMA]_

    The dialogue may give you hints on what you might wish to do.
    Here are some commands to try:

{0}

[DRAMA]_

    You can always choose to do nothing, simply by pressing *Return*.

.. property:: DRAMA.prompt ?
.. property:: DRAMA.state pot.types.Operation.prompt

History
-------

.. condition:: DRAMA.history[0].name do_history

[DRAMA]_

    Recent commands:

{0}

.. property:: DRAMA.state pot.types.Operation.prompt

Look
----

.. condition:: DRAMA.history[0].name do_look

[DRAMA]_

    |PLAYER_NAME| is in the |PLAYER_LOCN|.
    Looking around, he is aware of:

{0}

.. property:: DRAMA.state pot.types.Operation.prompt

.. |INPUT_TEXT| property:: DRAMA.input_text
.. |PLAYER_NAME| property:: PLAYER.name
.. |PLAYER_LOCN| property:: PLAYER.location.title
