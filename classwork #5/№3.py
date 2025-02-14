def f(x, n, k):
    if x > n+1:
        return 0
    elif x == n:
        return 1
    else:
        if k == 1:
            return f(x * 2, n, k-1) + f(x * 3, n, k-1)
        return f(x - 1, n, k+1) + f(x * 2, n, k) + f(x * 3, n, k)

print(f(3, 15, 0))