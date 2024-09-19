def f(n):
    if n < 3:
        return 1
    elif n > 2:
        return sum(f(i) for i in range(1, n))
print(f(18))