
file = open("input_2.txt", "r")
starting_point = 50
nb_zero = 0
print()
for line in file.readlines():
    print(starting_point)
    is_zero = starting_point == 0
    if line[0] == "L":
        starting_point -= int(line[1:])
    else:
        starting_point += int(line[1:])
    if not is_zero and (starting_point < 0 or starting_point >= 100):
        nb_zero += abs(starting_point // 100)

        starting_point = starting_point % 100
    else:
        nb_zero += (1 if starting_point == 0 else 0)
        starting_point = starting_point % 100
    print(line.strip(), nb_zero, starting_point, abs(int(starting_point / 100)) + (1 if starting_point <= 0 else 0),
          starting_point % 100)

print("result:", nb_zero)
starting_point = 50
nb_zero = 0
# dummy version

file = open("input_2.txt", "r")
for line in file.readlines():
    add = (-1 if line[0] == "L" else 1)
    for i in range(int(line[1:])):
        starting_point += add
        if starting_point % 100 == 0:
            nb_zero += 1

#pas 6643

print("result:", nb_zero)