a = [2, 3, 4, 5, 6, 1, 2, 3]

for i,v in enumerate(a):
    if v % 2 == 0:
        a[i] = 0

print(*a)

a = [2, 3, 4, 5, 6, 1, 2, 3]
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] = 0

print(*a)