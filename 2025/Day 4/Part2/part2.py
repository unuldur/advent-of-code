#file = open("../input_test", "r")
file = open("input.txt", "r")


lines = [line.strip() for line in file.readlines()]

max_height = len(lines)
max_width = len(lines[0])


def number_paper(x: int, y: int, lines):
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

def remove_rolls(lines):
    new_lines = [[c for c in line] for line in lines]
    nb_remove = 0
    for x, line in enumerate(lines):
        for y, character in enumerate(line):
            if character != '@':
                continue
            if number_paper(x, y, lines) < 4:
                new_lines[x][y] = '.'
                nb_remove += 1
    return new_lines, nb_remove


result = 0
new_lines, nb_remove = remove_rolls(lines)
while nb_remove > 0:
    result += nb_remove
    new_lines, nb_remove = remove_rolls(new_lines)

print("result", result)
