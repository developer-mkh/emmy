from munou.responder import responder


def _prompt(unmo_name, responder_name):
    return unmo_name + ":" + responder_name + "> "


class Proto:

    def __init__(self, name):
        self._name = name
        self.__responder = responder.Proto("what")

    def dialogue(self, input):
        return self.__responder.response(input)

    def responder_name(self):
        return self.__responder.name()

    def name(self):
        return self._name

    def prompt(self):
        return _prompt(self.name(), self.responder_name())





