def f(x, A):
    return ((x in A) <= (x ** 2 <= 81)) and ((x ** 2 <= 36) <= (x in A))


a = set([i for i in range(-1000, 1000)])

for x in range(-1000, 1000):
    if not f(x, a):
        a.remove(x)
print(len(a) - 1)