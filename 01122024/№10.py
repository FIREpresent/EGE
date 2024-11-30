def func(arr):
    print(arr)
    v = []
    for i in range(len(arr)):
        v.append(arr.count(arr[i]))
    print(v)
    print('-----------------------')

    if v.count(3) == 3 and v.count(1) == 3:
        summa_repeat = (sum(int(arr[i]) for i in range(len(v)) if v[i] == 3))**2
        summa = (sum(int(arr[i]) for i in range(len(v)) if v[i] == 1))**2
        if summa_repeat > summa:
            return 1
        return 0
    return 0

f = open('69915.csv', 'r')
lines = f.readlines()
count = 0
for line in lines:
    count += func(sorted(line.strip().split(',')))
f.close()
print(count)


# arr = ['146', '214', '27', '27', '27', '33']
# v = [1, 1, 3, 3, 3, 1]
#
# if v.count(3) == 1 and v.count(1) == 3:
#     summa_repeat = (sum(arr[i] for i in range(len(v)) if v[i] == 3)) ** 2
#     printI
#     summa = (sum(arr[i] for i in range(len(v)) if v[i] == 1)) ** 2
#     if summa_repeat > summa:
#         print('YES')
#     print('NO')
# print('NO')