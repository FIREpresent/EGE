def f(x, n):
    if x < n:
        return 0
    elif x == n:
        return 1
    return f(x-2, n) + f(x//2, n)

print(f(38, 16)*f(16, 2))