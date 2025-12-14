from typing import List

#file = open("../input_test", "r")
file = open("../input.txt", "r")


def read_file(lines: str):
    parts = lines.split("\n\n")
    shapes = []
    for part in parts[:-1]:
        shapes.append("\n".join([l.strip() for l in part.split("\n")[1:]]))
    regions = []
    for region in parts[-1].split("\n"):
        dimensions, numbers = region.split(": ")
        x, y = dimensions.split("x")
        regions.append(((int(x), int(y)), [int(n) for n in numbers.split(" ")]))
    return shapes, regions, [sum(ch == "#" for row in grid for ch in row) for grid in shapes]


shapes, regions, num_wal_shapes = read_file(file.read())
print(shapes, regions)


total = 0
for (x, y), num in regions:
    max_presents_lower_bound = (
            (x // 3) * (y // 3)
    )
    num_presents = sum(num)
    if num_presents <= max_presents_lower_bound:
        total += 1
        continue
    num_tiles_lower_bound = sum(
        tiles * quantity
        for tiles, quantity in zip(num_wal_shapes, num)
    )
    region_num_tiles = x * y
    if num_tiles_lower_bound > region_num_tiles:
        continue
    assert False, "Not working"

print("total", total)