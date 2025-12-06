import re
import math

#file = open("../input_test", "r")
file = open("input.txt", "r")


numbers, multiplicateurs = [], []
lines = file.readlines()


for line in lines[:-1]:
    line = [int(n) for n in re.split(r"\s+", line.strip())]
    if len(numbers) == 0:
        numbers = [[] for i in range(len(line))]
    for i, n in enumerate(line):
        numbers[i].append(n)


def calcul(parms: str, line):
    if parms == '+':
        return sum(line)
    return math.prod(line)

multiplicateurs = re.split(r"\s+", lines[-1])
print(numbers, multiplicateurs)

result = sum(calcul(param, line) for param, line in zip(multiplicateurs, numbers))

print(result)