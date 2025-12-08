import math

#file = open("../input_test", "r")
file = open("input.txt", "r")

points = [[int(p) for p in line.strip().split(',')] for line in file.readlines()]


distances = []

for i, point1 in enumerate(points):
    for point2 in points[i:]:
        if point1 == point2:
            continue
        distances.append((point1, point2, math.dist(point1, point2)))

distances.sort(key=lambda x: x[2])
boxes = []
for p1, p2, _ in distances[:1000]:
    box = [box for box in boxes if p1 in box or p2 in box]
    if len(box) == 0:
        boxes.append([p1, p2])
    elif len(box) == 1:
        points = box[0]
        if p1 not in points:
            points.append(p1)
        if p2 not in points:
            points.append(p2)
    else:
        new_box = []
        for v in box:
            boxes.remove(v)
            new_box.extend(v)
        if p1 not in new_box:
            new_box.append(p1)
        if p2 not in new_box:
            new_box.append(p2)
        boxes.append(new_box)

print(points)
print(distances)
print(boxes)
result = [len(box) for box in boxes]
result.sort()
result.reverse()
print("result", math.prod(result[:3]))

