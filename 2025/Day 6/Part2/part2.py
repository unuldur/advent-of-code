import re
import math

#file = open("../input_test", "r")
file = open("input.txt", "r")


numbers, multiplicateurs = [], []
lines = file.readlines()


def calcul(parms: str, line):
    numbers = [int(n if n.strip() != '' else 0) for n in line]
    if parms == '+':
        return sum(numbers)
    return math.prod(numbers)


for line in lines[:-1]:
    line = [int(n) for n in re.split(r"\s+", line.strip())]
    if len(numbers) == 0:
        numbers = [[] for i in range(len(line))]
    for i, n in enumerate(line):
        numbers[i].append(n)


multiplicateurs = re.split(r"\s+", lines[-1])
max_size_numbers = [max(len(str(a)) for a in number) for number in numbers]
numbers_right = [[] for i in range(len(numbers))]

current_index = 0
for i,max_size_number in enumerate(max_size_numbers):
    numbers_right[i] = ['' for _ in range(max_size_number)]
    for x in range(max_size_number):
        for y in range(len(lines) - 1):
            numbers_right[i][x] += lines[y][x + current_index]
    current_index += max_size_number + 1

print(numbers_right)
print(numbers, multiplicateurs, max_size_numbers)

result = sum(calcul(param, line) for param, line in zip(multiplicateurs, numbers_right))

print(result)