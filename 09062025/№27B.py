cl1 = []
cl2 = []
cl3 = []

def calculate_center(arr):
    center = 0
    min_dist = 10**10
    for star in arr:
        dist = 0
        for star2 in arr:
            dist += ((star[0] - star2[0])**2 + (star[1] - star2[1])**2)**0.5
        if dist < min_dist:
            min_dist = dist
            center = (star[0], star[1])
    return center

def calculate_anticenter(arr):
    anticenter = 0
    max_dist = -10**10
    for star in arr:
        dist = 0
        for star2 in arr:
            dist += ((star[0] - star2[0])**2 + (star[1] - star2[1])**2)**0.5
        if dist > max_dist:
            max_dist = dist
            anticenter = (star[0], star[1])
    return anticenter

with open('27B_22625.txt') as f:
    lines = f.readlines()
    for line in lines:
        x, y = line.split(' ')
        x, y = float(x), float(y)

        if y < 5:
            cl1.append((x, y))
        elif 5 < y < 20:
            cl2.append((x, y))
        elif y > 20:
            cl3.append((x, y))

x1, y1 = calculate_center(cl1)
x2, y2 = calculate_center(cl2)
x3, y3 = calculate_center(cl3)


x1_, y1_ = calculate_anticenter(cl1)
x2_, y2_ = calculate_anticenter(cl2)
x3_, y3_ = calculate_anticenter(cl3)

print(int(abs((x1 + x2 + x3) / 3 * 10_000)), int(abs((y1_ + y2_ + y3_) / 3 * 10_000)))
