f = open("27-B.txt")
n = int(f.readline())
v = []
for num in f:
    v.append(int(num))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if ((v[i] + v[j]) % 3 == 0) and ((v[i] * v[j]) % 1024 == 0):
            count += 1
f.close()
print(count)