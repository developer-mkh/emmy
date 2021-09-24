from builtins import print, input, len, FileNotFoundError, exit

from munou.unmo import unmo


file_path = "../work/random.txt"
try:
    _unmo = unmo.Proto("proto", file_path)
except FileNotFoundError as e:
    print('"' + file_path + '"' + " is not found.")
    exit(-1)

while True:
    word = input(_unmo.prompt())
    if len(word) == 0:
        break
    print(_unmo.dialogue(word))

print("バイバイ")
