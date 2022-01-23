import re

from munou.util import select_random


class Responder:
    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary

    def response(self, input_message, mood):
        return ""

    def name(self):
        return self._name


class WhatResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message, mood):
        return input_message + "ってなに？"


class RandomResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message, mood):
        return select_random(self._dictionary.random())


class PatternResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message, mood):
        for pattern_item in self._dictionary.pattern():
            result = pattern_item.match(input_message)
            if result is not None:
                resp = pattern_item.choice(mood)
                if resp is not None:
                    return re.sub("%match%", result.group(0), resp)

        return select_random(self._dictionary.random())
