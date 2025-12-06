#file = open("../input_test", "r")
file = open("input.txt", "r")

fresh_range, ingredients = file.read().split("\n\n")

fresh_range = [[int(i) for i in frange.split("-")] for frange in fresh_range.split("\n")]
ingredients = [int(i) for i in ingredients.split("\n")]


def merge_ranges(r1: range, r2: range) -> range:
    new_start = min(r1.start, r2.start)
    new_stop = max(r1.stop, r2.stop)
    return range(new_start, new_stop)


new_fresh_range = []
fresh_range.sort(key=lambda x: x[0])
for rng in fresh_range:
    mergins_range = [r for r in new_fresh_range if r.start <= rng[1] and rng[0] <= r.stop]
    new_range = range(rng[0], rng[1])
    if len(mergins_range) > 0:
        new_fresh_range = [r for r in new_fresh_range if r not in mergins_range]
        for r in mergins_range:
            new_range = merge_ranges(new_range, r)

    new_fresh_range.append(new_range)
    print(sum(rng.stop - rng.start + 1 for rng in new_fresh_range))

result = sum(rng.stop - rng.start + 1 for rng in new_fresh_range)
print(new_fresh_range)
print("result", result)


#Errors
# 345821388687076
# 345821388687084