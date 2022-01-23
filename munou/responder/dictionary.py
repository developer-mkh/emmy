import re

from munou.util import select_random


class Dictionary:
    def __init__(self, random_file_name, pattern_file_name):
        self._random = []
        with open(random_file_name, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.rstrip()
                if len(line) != 0:
                    self._random.append(line)

        self._pattern = []
        with open(pattern_file_name, "r", encoding="UTF-8") as f:
            for line in f:
                line = line.rstrip()
                if len(line) != 0:
                    line_split = line.split("\t")
                    if (len(line_split[0]) != 0) & (len(line_split[1]) != 0):
                        self._pattern.append(PatternItem(line_split[0], line_split[1]))

    def random(self):
        return self._random

    def pattern(self):
        return self._pattern


class PatternItem:
    SEPARATOR = "^((-?\d+)##)?(.*)$"

    def __init__(self, pattern, phrases):
        result = re.match(self.SEPARATOR, pattern)
        self._pattern = result.group(3)
        if result.group(2) is not None:
            self._modify = int(result.group(2))
        else:
            self._modify = 0

        self._phrases = []
        for phrase in phrases.split("|"):
            result = re.match(self.SEPARATOR, phrase)
            need = 0
            if result.group(2) is not None:
                need = int(result.group(2))
            self._phrases.append({"need": need, "phrase": result.group(3)})

    def match(self, param):
        return re.match(self._pattern, param)

    def choice(self, mood):
        choices = []
        for phrase in self._phrases:
            if self.suitable(phrase["need"], mood):
                choices.append(phrase["phrase"])
        return None if len(choices) == 0 else select_random(choices)

    def suitable(self, need, mood):
        ret = False
        if need > 0:
            ret = mood > need
        elif need < 0:
            ret = mood < need
        else:
            ret = True
        return ret

    def modify(self):
        return self._modify

    def pattern(self):
        return self._pattern

    def phrases(self):
        return self._phrases
