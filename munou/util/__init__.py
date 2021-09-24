from builtins import len

import random


def select_random(array):
    return array[random.randint(0, len(array) - 1)]
