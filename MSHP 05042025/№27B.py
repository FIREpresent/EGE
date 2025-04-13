f = open('27_B.csv')

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
D = []

for point in vec:

    x = point[0]
    y = point[1]

    if y > 1.2 * x and y > 8 - x:
        A.append(point)
    elif y < 1.2 * x and y > 8 - x:
        B.append(point)
    elif y > 1.2 * x and y < 8 - x:
        C.append(point)
    elif y < 1.2 * x and y < 8 - x:
        D.append(point)

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

min_sum_D = 10 ** 10
min_sum_point_D = []

for i in range(len(D)):
    current_point = D[i]
    cur_sum = 0
    for j in range(len(D)):
        if i == j:
            continue
        distance = ((D[j][0] - D[i][0]) ** 2 + (D[j][1] - D[i][1]) ** 2) ** 0.5
        cur_sum += distance

    if cur_sum < min_sum_D:
        min_sum_D = cur_sum
        min_sum_point_D = current_point

R_A = -10 ** 10
for i in range(len(A)):
    current_point = A[i]
    distance = ((min_sum_point_A[0] - A[i][0]) ** 2 + (min_sum_point_A[1] - A[i][1]) ** 2) ** 0.5
    R_A = max(R_A, distance)

R_B = -10 ** 10
for i in range(len(B)):
    current_point = B[i]
    distance = ((min_sum_point_B[0] - B[i][0]) ** 2 + (min_sum_point_B[1] - B[i][1]) ** 2) ** 0.5
    R_B = max(R_B, distance)

R_C = -10 ** 10
for i in range(len(C)):
    current_point = C[i]
    distance = ((min_sum_point_C[0] - C[i][0]) ** 2 + (min_sum_point_C[1] - C[i][1]) ** 2) ** 0.5
    R_C = max(R_C, distance)

R_D = -10 ** 10
for i in range(len(D)):
    current_point = D[i]
    distance = ((min_sum_point_D[0] - D[i][0]) ** 2 + (min_sum_point_D[1] - D[i][1]) ** 2) ** 0.5
    R_D = max(R_D, distance)

R = (R_A + R_B + R_C + R_D) / 4
print(int(R * 10_000))
