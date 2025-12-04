#file = open("../input_test", "r")
file = open("input.txt", "r")


lines = [line.strip() for line in file.readlines()]

max_height = len(lines)
max_width = len(lines[0])


def number_paper(x: int, y: int):
    number = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i == x and j == y:
                continue
            if i < 0 or i >= max_height:
                continue
            if j < 0 or j >= max_width:
                continue
            if lines[i][j] == '@':
                number += 1
    return number


result = 0
for x, line in enumerate(lines):
    for y, character in enumerate(line):
        if character != '@':
            continue
        if number_paper(x, y) < 4:
            result += 1
print("result", result)
