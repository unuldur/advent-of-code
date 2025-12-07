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


lasers = dict()
lasers[start] = 1
for spliters_line in spliters:
    pos_laser = lasers.keys()
    spliters_activate = [splitter for splitter in spliters_line if splitter in pos_laser]
    new_lasers = dict()
    for pos in pos_laser:
        if pos not in spliters_activate:
            new_lasers[pos] = lasers[pos]
    for spliter in spliters_activate:
        if spliter - 1 not in new_lasers.keys():
            new_lasers[spliter - 1] = 0
        new_lasers[spliter - 1] += lasers[spliter]
        if spliter + 1 not in new_lasers.keys():
            new_lasers[spliter + 1] = 0
        new_lasers[spliter + 1] += lasers[spliter]
    lasers = new_lasers

print(start, spliters, lasers)
print("result", sum([val for val in lasers.values()]))

