def check(arr):
    arr2 = [x for x in arr]
    v = []
    summ = 0
    for i in range(len(arr2)):
        same = 0
        for j in range(len(arr2)):
            if arr2[i] == arr2[j]:
                same += 1
        v.append(same)
    for i in range(len(v)):
        if v[i] == 2:
            summ += (v[i]-1)*arr2[i]
        elif v[i] == 3:
            summ += (v[i]-2)*arr2[i]
    if summ < max(arr2):
        v.clear()
        return 1

    v.clear()
    return 0

def func(arr):
    if (len(arr) != len(set(arr))) and (arr.count(max(arr)) == 1) and check(arr):
        return 1
    return 0

f = open('09.csv', 'r')
lines = f.readlines()
count = 0
for line in lines:
    count += func(list(map(int, line.strip().split(','))))
f.close()
print(count)