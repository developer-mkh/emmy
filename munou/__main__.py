from builtins import print, input, len

from munou.unmo import unmo


_unmo = unmo.Proto("proto")

while True:
    word = input(_unmo.prompt())
    if len(word) == 0:
        break
    print(_unmo.dialogue(word))

print("バイバイ")
