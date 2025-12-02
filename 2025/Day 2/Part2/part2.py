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
    already_done = set()
    for n in range(10**max_val):
        mult = len(rng_max) // len(str(n)) + 2
        for i in range(2, mult):
            val = int(str(n) * i)
            if val in already_done:
                continue
            if mi <= val <= ma:
                result += val
                already_done.add(val)

print("result:", result)
# response:  34284458938
# nope : 34284458980