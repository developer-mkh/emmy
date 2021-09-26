import random

from munou.responder import responder, dictionary


def _prompt(name):
    return name + "> "


class Proto:

    def __init__(self, name, random_file_name, pattern_file_name):
        self._name = name
        self._dictionary = dictionary.Dictionary(random_file_name, pattern_file_name)

        self._resp_what = responder.WhatResponder("what", self._dictionary)
        self._resp_random = responder.RandomResponder("Random", self._dictionary)
        self._resp_pattern = responder.PatternResponder("Pattern", self._dictionary)

        self._responder = self._resp_pattern

    def dialogue(self, input_message):
        probability = random.randint(0, 99)
        if probability <= 59:
            self._responder = self._resp_pattern
        elif probability <= 89:
            self._responder = self._resp_random
        else:
            self._responder = self._resp_what

        return self._responder.response(input_message)

    def responder_name(self):
        return self._responder.name()

    def name(self):
        return self._name

    def prompt(self):
        return _prompt("Emmy")





