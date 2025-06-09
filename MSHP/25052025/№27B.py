from math import dist

with open('27-1b.txt') as f:
    next(f)
    data = [tuple(map(float, line.split())) for line in f]


def get_medoid(cluster):
    return min(cluster,
               key=lambda p: sum(dist(p, q) for q in cluster))


def dbscan(data, eps):
    clusters = []

    while data:
        point = data.pop()
        cluster = [point]
        queue = [point]

        while queue:
            current = queue.pop(0)
            neighbors = [p for p in data if
                         dist(current, p) < eps]
            cluster.extend(neighbors)
            queue.extend(neighbors)
            data[:] = [p for p in data if
                       p not in neighbors]

        clusters.append(cluster)

    return clusters


clusters = dbscan(data, 0.3)
print(f'До фильтрации: {[len(cluster) for cluster in clusters]}')

clusters = [cluster for cluster in clusters if len(cluster) > 13]
print(f'После фильтрации: {[len(cluster) for cluster in clusters]}')

medoids = [get_medoid(cluster) for cluster in clusters]

px = sum(x for x, y in medoids) / len(medoids)
py = sum(y for x, y in medoids) / len(medoids)

print(abs(int(px * 10_000)), abs(int(py * 10_000)))

#До фильтрации: [3326, 3328, 3330, 5, 2, 3, 4]
#После фильтрации: [3326, 3328, 3330]
#41107 48687