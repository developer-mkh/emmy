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
                        self._pattern.append(line_split)

    def random(self):
        return self._random

    def pattern(self):
        return self._pattern
