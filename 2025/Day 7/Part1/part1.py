#file = open("../input_test", "r")
file = open("input.txt", "r")

start = 0
spliters = []

for i, line in enumerate(file.readlines()):
    if i == 0:
        index = line.index('S')
        start = index
    else:
        indexes = [i for i, c in enumerate(line) if c == '^']
        if len(indexes) > 0:
            spliters.append(indexes)


lasers = set()
lasers.add(start)
result = 0
for spliters_line in spliters:
    spliters_activate = [splitter for splitter in spliters_line if splitter in lasers]
    lasers = set([laser for laser in lasers if laser not in spliters_activate])
    for spliter in spliters_activate:
        lasers.add(spliter - 1)
        lasers.add(spliter + 1)
    result += len(spliters_activate)


print(start, spliters, lasers)
print("result", result)

