def func(a, b, c):
    k = 0
    if len(str(a)) == 3:
        k += 1
    if len(str(b)) == 3:
        k += 1
    if len(str(c)) == 3:
        k += 1
    return k

f = open('17.txt')
vec = [int(i) for i in f]

count = 0
maximum_sum, maximum = -1*10**10, -1*10**10

for i in range(len(vec)):
    if vec[i] % 100 == 13:
        maximum = max(maximum, vec[i])

for i in range(len(vec) - 2):
    if func(vec[i], vec[i+1], vec[i+2]) == 2 and sum([vec[i], vec[i+1], vec[i+2]]) <= maximum:
        maximum_sum = max(maximum_sum, sum([vec[i], vec[i+1], vec[i+2]]))
        count += 1
print(count, maximum_sum)
