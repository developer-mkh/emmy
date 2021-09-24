class Proto:
    def __init__(self, name):
        self._name = name

    def response(self, input):
        return input + "ってなに？"

    def name(self):
        return self._name
