from builtins import open
from munou.util import select_random


class Responder:
    def __init__(self, name):
        self._name = name

    def response(self, input):
        return ""

    def name(self):
        return self._name


class WhatResponder(Responder):
    def __init__(self, name):
        Responder.__init__(self, name)

    def response(self, input):
        return input + "ってなに？"


class RandomResponder(Responder):
    def __init__(self, my_name, dictionary_file_name):
        Responder.__init__(self, my_name)
        self._response = []
        with open(dictionary_file_name, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.rstrip()
                if line != "":
                    self._response.append(line)

    def response(self, input):
        return select_random(self._response)
