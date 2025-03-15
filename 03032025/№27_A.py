
f = open('27A.csv')
k = f.readline()
lines = f.readlines()
vec = []

for line in lines:
    temp_vec = line.strip().split()
    temp_vec[0] = temp_vec[0].replace(',', '.', 1)
    temp_vec[1] = temp_vec[1].replace(',', '.', 1)

    temp_vec = list(map(float, temp_vec))

    vec.append(temp_vec)

A = []
B = []
C = []

for point in vec:
    if point[1] < 2:
        A.append(point)
    elif 2 < point[1] < 6:
        B.append(point)
    elif 6 < point[1]:
        C.append(point)

min_sum_A = 10 ** 10
min_sum_point_A = []

for i in range(len(A)):
    current_point = A[i]
    cur_sum = 0
    for j in range(len(A)):
        if i == j:
            continue
        distance = ((A[j][0] - A[i][0]) ** 2 + (A[j][1] - A[i][1]) ** 2) ** 0.5
        cur_sum += distance

    if cur_sum < min_sum_A:
        min_sum_A = cur_sum
        min_sum_point_A = current_point

min_sum_B = 10 ** 10
min_sum_point_B = []

for i in range(len(B)):
    current_point = B[i]
    cur_sum = 0
    for j in range(len(B)):
        if i == j:
            continue
        distance = ((B[j][0] - B[i][0]) ** 2 + (B[j][1] - B[i][1]) ** 2) ** 0.5
        cur_sum += distance

    if cur_sum < min_sum_B:
        min_sum_B = cur_sum
        min_sum_point_B = current_point

min_sum_C = 10 ** 10
min_sum_point_C = []

for i in range(len(C)):
    current_point = C[i]
    cur_sum = 0
    for j in range(len(C)):
        if i == j:
            continue
        distance = ((C[j][0] - C[i][0]) ** 2 + (C[j][1] - C[i][1]) ** 2) ** 0.5
        cur_sum += distance

    if cur_sum < min_sum_C:
        min_sum_C = cur_sum
        min_sum_point_C = current_point

print(int((min_sum_point_A[0] + min_sum_point_B[0] + min_sum_point_C[0])/3 * 10_000), int((min_sum_point_A[1] + min_sum_point_B[1] + min_sum_point_C[1])/3 * 10_000))
