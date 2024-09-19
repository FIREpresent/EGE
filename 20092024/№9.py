def check(arr):
    arr2 = arr[::]
    v = []
    c = 0
    summ = 0
    for i in range(len(arr)):
        same = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                same += 1
        v.append(same)

    for i in range(len(v)):
        if v[i] == 2:
            c += 1
            summ += (v[i] - 1) * arr[i]
            arr2.remove(arr[i])
        elif v[i] == 3:
            c += 1
            summ += (v[i] - 2) * arr[i]
            arr2.remove(arr[i])
        elif v[i] == 4:
            c += 1
            summ += (v[i] - 3) * arr[i]
            arr2.remove(arr[i])
        elif v[i] == 5:
            c += 1
            summ += (v[i] - 4) * arr[i]
            arr2.remove(arr[i])


    if c == 0:
        c = 1

    if len(arr2) == 0:
        arr2.append(1)

    if summ/c < sum(arr2)/len(arr2):
        v.clear()
        return 1

    v.clear()
    return 0

def func(x):
    if len(set(x)) != len(x) and check(x) == 1:
        return 1
    return 0

f = open("09.csv")
lines = f.readlines()
count = 0
for line in lines:

    count += func(list(map(int, line.strip().split(','))))
f.close()
print(count)
