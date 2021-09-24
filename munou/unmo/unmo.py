import random

from munou.responder import responder


def _prompt(name):
    return name + "> "


class Proto:

    def __init__(self, name, dictionary_file_name):
        self._name = name
        self._resp_what = responder.WhatResponder("what")
        self._resp_random = responder.RandomResponder("Random", dictionary_file_name)
        self._responder = self._resp_random

    def dialogue(self, input):
        self._responder = self._resp_what if random.randint(0, 1) == 0 else self._resp_random
        return self._responder.response(input)

    def responder_name(self):
        return self._responder.name()

    def name(self):
        return self._name

    def prompt(self):
        return _prompt("Emmy")





