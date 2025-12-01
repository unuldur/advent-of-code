
file = open("input_2.txt", "r")
starting_point = 50
nb_zero = 0

for line in file.readlines():
    if line[0] == "L":
        starting_point -= int(line[1:])
    else:
        starting_point += int(line[1:])
    if starting_point < 0 or starting_point >= 100:
        nb_zero += abs(starting_point // 100)
    print(line, nb_zero, starting_point, starting_point // 100, starting_point % 100)
    starting_point = starting_point % 100


print("result:", nb_zero)