from math import dist
import turtle

with open('27-1b.txt') as file:
    next(file)
    data = [list(map(float, line.split())) for line in file]

def assign_clusters(data, centers):
    labels = []
    for p in data:
        distances = [dist(p, center) for center in centers]
        labels.append(distances.index(min(distances)))
    return labels


def update_centers(data, labels, k):
    new_centers = []
    for cluster_label in range(k):
        cluster = [p for p, l in zip(data, labels)
                   if l == cluster_label]
        medoid = min(cluster, key=lambda p:
        sum(dist(p, q) for q in cluster))
        new_centers.append(medoid)
    return new_centers


def k_means(data, k):
    centers = [[2, 2], [-1, -1], [2, 7]]
    new_centers = []
    while new_centers != centers:
        labels = assign_clusters(data, centers)
        new_centers = update_centers(data, labels, k)
        centers = new_centers
    return labels, centers


labels, centers = k_means(data, 3)


def draw_scatter(data, labels):
    turtle.screensize(2000, 2000)
    turtle.tracer(0)
    scale = 50
    colors = ["#F76D47", "#A7D380", "#79CFD4"]
    for point, label in zip(data, labels):
        turtle.setpos(point[0] * scale, point[1] * scale)
        turtle.dot(16, colors[label])
    turtle.update()
    turtle.done()


draw_scatter(data, labels)

px = sum(x for x, y in centers) / len(centers)
py = sum(y for x, y in centers) / len(centers)

print(abs(int(px * 10_000)), abs(int(py * 10_000)))