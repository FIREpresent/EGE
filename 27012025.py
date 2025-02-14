arr = []

cluster1 = []
cluster2 = []
for point in arr:
    x = point[0]
    y = point[1]

    if x < 1 and y < 3:
        cluster1.append((x, y))
    elif x > 1 and y > 3:
        cluster2.append((x, y))

