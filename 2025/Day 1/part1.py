
file = open("input_1.txt", "r")
starting_point = 50
nb_zero = 0

for line in file.readlines():
    if line[0] == "L":
        starting_point -= int(line[1:])
    else:
        starting_point += int(line[1:])
    starting_point = starting_point % 100
    print(starting_point)
    if starting_point == 0:
        nb_zero += 1

print("result:", nb_zero)