import re

from munou.util import select_random


class Responder:
    def __init__(self, name, dictionary):
        self._name = name
        self._dictionary = dictionary

    def response(self, input_message):
        return ""

    def name(self):
        return self._name


class WhatResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message):
        return input_message + "ってなに？"


class RandomResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message):
        return select_random(self._dictionary.random())


class PatternResponder(Responder):
    def __init__(self, name, dictionary):
        Responder.__init__(self, name, dictionary)

    def response(self, input_message):
        for line in self._dictionary.pattern():
            m = re.search(line[0], input_message)
            if m is not None:
                resp = select_random(line[1].split("|"))
                return re.sub("%match%", m.group(0), resp)

        return select_random(self._dictionary.random())
