#!/usr/bin/env python3
# encoding: utf-8

# This is a parser-based text adventure.
# Copyright (C) 2021 D E Haynes

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from collections import defaultdict
import string
import unittest

from turberfield.catchphrase.presenter import Presenter
from turberfield.dialogue.model import SceneScript

from pot.story import Story

class Witness(Presenter):

    @classmethod
    def represent(cls, story, *args, facts=None, previous=None, **kwargs):
        rv = story.context.interlude(
            story.context.folder,
            previous and previous.index,
            previous and previous.ensemble
        )
        return cls.build_presenter(
            story.context.folder, *args, facts=facts or rv,
            ensemble=story.context.ensemble + [story.context, story.settings],
            **kwargs
        )

    @staticmethod
    def build_presenter(folder, *args, facts=None, ensemble=None, strict=True, roles=1):
        rv = None
        paths = getattr(folder, "paths", folder)
        pkg = getattr(folder, "pkg", None)
        print("Paths", paths, pkg)
        for n, p in enumerate(paths):
            text = Presenter.load_dialogue(pkg, p)
            text = string.Formatter().vformat(text, args, facts or defaultdict(str))
            rv = Witness.build_from_text(
                text, index=n, ensemble=ensemble or [], strict=strict, roles=roles, path=p
            )
            if rv:
                break

        return rv

    @staticmethod
    def build_from_text(text, index=None, ensemble=[], strict=True, roles=1, path="inline"):
        script = SceneScript(path, doc=SceneScript.read(text))
        selection = script.select(ensemble, roles=roles)
        print(list(selection.keys()), all(selection.values()))
        if all(selection.values()) or (not strict and any(selection.values())):
            script.cast(selection)
            casting = {next(iter(i.attributes.get("names", [])), None): i.persona for i in selection}
            print(list(casting.keys()), all(casting.values()))
            model = script.run()
            rv = Presenter(model, index=index, casting=casting, ensemble=ensemble, text=text)
            for k, v in model.metadata:
                rv.metadata[k].append(v)
            return rv


class StoryTests(unittest.TestCase):

    def setUp(self):
        self.story = Story()

    def test_story(self):
        reply = ""
        for n, cmd in enumerate(["go w", "look", "look"]):
            with self.subTest(n=n, cmd=cmd):
                presenter = Witness.represent(self.story, reply)
                self.assertTrue(
                    presenter, "\n".join(f"{i!s} {i._states}" for i in self.story.context.ensemble)
                )
                print("Player:", vars(self.story.context.player))
                print("World:", list(self.story.context.world.lookup.keys()))

                animation = next(filter(None, (presenter.animate(f) for f in presenter.frames if f)))
                text = "\n".join(l for l, d in self.story.render_frame_to_terminal(animation))
                reply = self.story.context.deliver(cmd, presenter=presenter)
                print(reply)
