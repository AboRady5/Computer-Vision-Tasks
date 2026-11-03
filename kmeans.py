import math

points = [
    (1, 1),
    (2, 1),
    (1, 2),
    (6, 5),
    (7, 5),
    (6, 6)
]

k = 2

centers = [
    (1, 1),
    (2, 1)
]


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


while True:
    groups = [[] for _ in range(k)]

    for p in points:
        best = 0

        for i in range(1, k):
            if distance(p, centers[i]) < distance(p, centers[best]):
                best = i

        groups[best].append(p)

    new_centers = []

    for group in groups:
        x = sum(p[0] for p in group) / len(group)
        y = sum(p[1] for p in group) / len(group)

        new_centers.append((x, y))

    if new_centers == centers:
        break

    centers = new_centers


for i in range(k):
    print(f"Cluster {i + 1}: {groups[i]}")
    print(f"Center: {centers[i]}")
    print()
