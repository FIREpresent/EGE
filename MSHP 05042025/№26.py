N, S = input().split()
N, S = int(N), int(S)
k = []
for i in range(N):
    num, w = input().split()
    k.append((num, int(w)))

k.sort(key=lambda x: x[0])

v = []
arr = []
k.append((-100, -100))
for i in range(len(k)):
    if i != 0:
        if k[i][0] != k[i-1][0]:
            v.append(sorted(arr, key=lambda x: x[1]))
            arr = [k[i]]
        else:
            arr.append(k[i])
    else:
        arr.append(k[i])

dels = []
for elem in v:
    summ = 0
    for i in range(len(elem)):
        if summ + elem[i][1] <= S:
            summ += elem[i][1]
            dels.append(elem[i])

for i in range(len(dels)):
    if dels[i] in v:
        v.pop(arr.index(dels[i]))

counter = 0
maximum = -10**10
for i in range(len(v)):
    if len(v[i]) > 0:
        counter += len(v[i][-1][0])
        maximum = max()





# 8 13
# 150 8
# 237 3
# 237 6
# 150 4
# 237 5
# 237 6
# 150 3
# 150 3