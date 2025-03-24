def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 3 == 2:
            return f(n-1) + 1
        elif n % 3 < 2:
            return f((n - (n % 3))/3)

for n in range(0, 1_000):
    if f(n) == 6:
        print(n)
        break