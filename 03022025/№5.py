count = 0
for i in range(100, 1000):
    s = ''.join(str(i))
    v = list(map(int, list(s)))
    num1, num2 = v[0] + v[1], v[1] + v[2]
    vec = sorted([num1, num2])
    if vec[0] == 12 and vec[1] == 16:
        count += 1
print(count)