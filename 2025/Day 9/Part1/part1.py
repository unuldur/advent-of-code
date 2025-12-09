#file = open("../input_test", "r")
file = open("input.txt", "r")

points = [[int(p) for p in line.strip().split(',')] for line in file.readlines()]

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

distances = []

for i, point1 in enumerate(points):
    for point2 in points[i:]:
        if point1 == point2:
            continue
        distances.append((point1, point2, area(point1, point2)))

distances.sort(key=lambda x: -x[2])
print(distances[0])