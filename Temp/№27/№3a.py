cl1, cl2, cl3 = [], [], []

# def find_cl_center(cl):
#     min_dist = 10**5
#     for star in cl:
#         dist = 0
#         for star2 in cl:
#             dist += ((star[0] - star2[0])**2 + (star[1] - star2[1])**2)**0.5
#         if dist < min_dist:
#             min_dist = dist
#             center = (star[0], star[1])
#     return center

def find_cl_center(cl):
    min_dist = 10**5
    for star in cl:
        max_dist = -10**10
        for star2 in cl:
            max_dist = max(max_dist, ((star[0] - star2[0])**2 + (star[1] - star2[1])**2)**0.5)
        if max_dist < min_dist:
            min_dist = max_dist
            center = (star[0], star[1])
    return center

with open('27-3a.txt') as f:
    for line in f:
        x, y = list(map(float, line.split()))
        if y > 2:
            cl1.append((x, y))
        elif -2 < y < 2:
            cl2.append((x, y))
        elif y < -2:
            cl3.append((x, y))

x1, y1 = find_cl_center(cl1)
x2, y2 = find_cl_center(cl2)
x3, y3 = find_cl_center(cl3)
print(x1, y1)
print(x2, y2)
print(x3, y3)

print(int(min(
    ((x1 - x2)**2 + (y1 - y2)**2)**0.5,
    ((x2 - x3)**2 + (y2 - y3)**2)**0.5,
    ((x3 - x1)**2 + (y3 - y1)**2)**0.5
)*10_000))

minimum = 10**10
arr = [(x1, y1), (x2, y2), (x3, y3)]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if i != j:
            minimum = min(minimum, ((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)**0.5)

print(int(minimum*10_000))