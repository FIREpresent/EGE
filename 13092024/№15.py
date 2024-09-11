def func(x, plenty):
    if ((x in plenty) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in plenty)):
        return 1
    return 0

plenty = [i for i in range(-10000, 10000)]
v = []
for i in range(-10000, 10000):
    if func(i, plenty):
        v.append(i)
print(v[-1] - v[0])