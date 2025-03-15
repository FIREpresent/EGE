N = int(input())
vec = []
answer_vec = []
flag_array = [True for i in range(N)]

for i in range(N):
    vec.append(list(map(int, input().split())))

for i in range(len(vec)):
    S = vec[i][0]
    P = vec[i][1]

    A = (P + (P**2 - 16*S)**0.5)//4
    B = (P - (P**2 - 16*S)**0.5)//4

    if A < B or A <= 0 or B <= 0:
        flag_array[i] = False

    if flag_array[i]:
        answer_vec.append([int(A), int(B)])
    else:
        answer_vec.append([0, 0])

for elem in answer_vec:
    print(*elem)
