f = open('1_17.txt')
v = [int(num) for num in f]
m = min([x for x in v if x % 19 == 0])
c = 0
maximum = 0
for i in range(len(v)-1):
    if (v[i] % m == 0) or (v[i+1] % m == 0):
        c += 1
        maximum = max(maximum, v[i] + v[i+1])
print(c, maximum)