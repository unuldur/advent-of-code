#file = open("../input_test", "r")
file = open("input.txt", "r")


def get_number(line: str, index_prev: int, count: int):
    if count == 0:
        return ''
    number = max(int(c) for c in line[(index_prev+1):(len(line) - count + 1)])
    index = line[(index_prev+1):].find(str(number)) + index_prev + 1
    return str(number) + get_number(line, index, count-1)


result = 0
for line in file.readlines():
    joltage = int(get_number(line.strip(), -1, 12))
    print(line, joltage)
    result += joltage

print('result : ', result)
