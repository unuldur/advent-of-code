#file = open("../input_test", "r")
file = open("input.txt", "r")

fresh_range, ingredients = file.read().split("\n\n")

fresh_range = [[int(i) for i in frange.split("-")] for frange in fresh_range.split("\n")]
ingredients = [int(i) for i in ingredients.split("\n")]

result = 0
for ingredient in ingredients:
    if any(rng[0] <= ingredient <= rng[1] for rng in fresh_range):
        result += 1

print("result", result)
