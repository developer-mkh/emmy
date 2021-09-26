from builtins import print, input, len, FileNotFoundError, exit

from munou.unmo import emmy


random_file_path = "../work/random.txt"
pattern_file_path = "../work/pattern.txt"

try:
    _unmo = emmy.Proto("proto", random_file_path, pattern_file_path)
except FileNotFoundError as e:
    print('"' + random_file_path + '"' + " or " + '"' + pattern_file_path + '"' + " is not found.")
    exit(-1)

while True:
    word = input(_unmo.prompt())
    if len(word) == 0:
        break
    print(_unmo.dialogue(word))

print("バイバイ")
