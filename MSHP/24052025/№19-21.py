def f(a, m):
    if a >= 59:
        return m % 2 == 0
    if m == 0:
        return 0
    l = [f(a+1, m-1), f(a+4, m-1), f(a*3, m-1)]
    return any(l) if (m-1) % 2 == 0 else all(l)

print(19, [s for s in range(1, 58+1) if f(s, 2)])
print(20, [s for s in range(1, 58+1) if not f(s, 1) and f(s, 3)])
print(21, [s for s in range(1, 58+1) if not f(s, 2) and f(s, 4)])
