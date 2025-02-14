def f(x, n):
    if x > n or x == 19:
        return 0
    elif x == n:
        return 1
    return f(x+1, n) + f(x+2, n) + f(x+3, n)

print(f(1, 7)*f(7, 35))