cl1, cl2, cl3 = [], [], []

def find_cl_center(cl):
    min_dist = 10**5
    for star in cl:
        dist = 0
        for star2 in cl:
            dist += ((star[0] - star2[0])**2 + (star[1] - star2[1])**2)**0.5
        if dist < min_dist:
            min_dist = dist
            center = (star[0], star[1])
    return center

with open('27-4b.txt') as f:
    for line in f:
        x, y = list(map(float, line.split()))
        if 0.5 < x < 5.5 and -3.5 < y < 1.5:
            cl1.append((x, y))
        elif -3.5 < x < -1.25 and -3.5 < y < 1:
            cl2.append((x, y))
        elif -1.75 < x < 3.75 and 1.8 < y < 4.1:
            cl3.append((x, y))

x1, y1 = find_cl_center(cl1)
x2, y2 = find_cl_center(cl2)
x3, y3 = find_cl_center(cl3)
print(x1, y1)
print(x2, y2)
print(x3, y3)

print(int((x1 + x2 + x3) / 3 * 10000))
print(int((y1 + y2 + y3) / 3 * 10000))
