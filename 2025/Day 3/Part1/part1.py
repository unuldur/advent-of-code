#file = open("../input_test", "r")
file = open("input.txt", "r")


def get_number(line: str):
    number_1 = max(int(c) for c in line[:-1])
    index_1 = line.find(str(number_1))
    number_2 = max(int(c) for c in line[(index_1 + 1):])

    return int(str(number_1) + str(number_2))


result = 0
for line in file.readlines():
    result += get_number(line.strip())

print('result : ', result)
