def f(a, b, m):
    if a+b >= 231: return m % 2 == 0
    if m == 0:
        return 0
    k = [f(a+2, b, m-1), f(a*2, b, m-1), f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(k) if (m-1)%2 == 0 else all(k)
    # return any(k) if (m-1)%2 == 0 else any(k)

print(19, [s for s in range(1, 213+1) if f(17, s, 2)])
print(20, [s for s in range(1, 128+1) if not f(17, s, 1) and f(17, s, 3)])
print(21, [s for s in range(1, 128+1) if not f(17, s, 2) and f(17, s, 4)])