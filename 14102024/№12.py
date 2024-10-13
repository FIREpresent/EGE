def func1(arr):
    v = []
    for x in arr:
        v.append(arr.count(x)-1)
    if v.count(1) == 2 and v.count(0) == 4:
        return 1 * func2(arr, v)
    return 0

def func2(arr, v):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr)):
        if v[i] == 1:
            sum1 += arr[i]
        else:
            sum2 += arr[i]

    return (sum1)/2 < (sum2)/4

f = open('093.csv')
lines = f.readlines()
c = 0
for line in lines:
    line = list(map(int, line.strip().split(',')))
    if func1(line):
        c += 1
f.close()
print(c)