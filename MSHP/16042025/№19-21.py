def f(a, b, m):
    if a+b >= 69:
        return m % 2 == 0
    if m == 0:
        return 0
    l = [f(a+2, b, m-1), f(a*2, b, m-1), f(a, b+2, m-1), f(a, b*2, m-1)]
    return any(l) if (m-1) % 2 == 0 else all(l)
    #return any(l) if (m-1) % 2 == 0 else any(l)

print(19, [s for s in range(1, 59+1) if f(9, s, 2)])
print(20, [s for s in range(1, 59+1) if not f(9, s, 1) and f(9, s, 3)])
print(21, [s for s in range(1, 59+1) if not f(9, s, 2) and f(9, s, 4)])