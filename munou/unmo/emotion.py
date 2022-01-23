import re


class Emotion:
    MOOD_MIN = -15
    MOOD_MAX = 15
    MOOD_RECOVERY = 0.5

    def __init__(self, dictionary_obj):
        self._dictionary = dictionary_obj
        self._mood = 0

    def update(self, input_message):
        for pattern in self._dictionary.pattern():
            m = pattern.match(input_message)
            if m is not None:
                self.adjust_mood(pattern.modify())
                break

        if self._mood < 0:
            self._mood += self.MOOD_RECOVERY
        elif self._mood > 0:
            self._mood -= self.MOOD_RECOVERY

    def adjust_mood(self, val):
        self._mood += val
        if self._mood > self.MOOD_MAX:
            self._mood = self.MOOD_MAX
        elif self._mood < self.MOOD_MIN:
            self._mood = self.MOOD_MIN

    def mood(self):
        return self._mood
