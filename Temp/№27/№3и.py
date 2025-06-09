cl1, cl2, cl3, cl4, cl5 = [], [], [], [], []

# def find_cl_center(cl):
#     center = ()
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

with open('27-3b.txt') as f:
    for line in f:
        x, y = list(map(float, line.split()))
        if x < -1:
            if y > 0:
                cl1.append((x, y))
            else:
                cl2.append((x, y))
        elif x > -1:
            if y > 1.4:
                cl3.append((x, y))
            elif -1.5 < y < 1.4:
                cl4.append((x, y))
            elif y < -1.5:
                cl5.append((x, y))

x1, y1 = find_cl_center(cl1)
x2, y2 = find_cl_center(cl2)
x3, y3 = find_cl_center(cl3)
x4, y4 = find_cl_center(cl4)
x5, y5 = find_cl_center(cl5)
print(x1, y1)
print(x2, y2)
print(x3, y3)
print(x4, y4)
print(x5, y5)

minimum = 10**10
arr = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if i != j:
            minimum = min(minimum, ((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)**0.5)

print(int(minimum*10_000))
