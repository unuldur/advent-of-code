import math

#file = open("../input_test", "r")
file = open("input.txt", "r")
ranges = file.readlines()[0].strip().split(',')
result = 0

for rng in ranges:
    rng_min, rng_max = rng.split('-')
    mi = int(rng_min)
    ma = int(rng_max)
    min_val = math.ceil(len(rng_min) / 2) - 1
    max_val = math.floor(len(rng_max) / 2)
    for n in range(10**min_val, 10**max_val):
        val = int(str(n) + str(n))
        if mi <= val <= ma:
            print(val)
            result += val


print("result:", result )