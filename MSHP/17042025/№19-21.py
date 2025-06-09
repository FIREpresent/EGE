def f(a, m):
    if a >= 43 and a < 72:
        return m % 2 == 0
    if a >= 72:
        return 1
    if m == 0:
        return 0
    l = [f(a+1, m-1), f(a*2, m-1), f(a*3, m-1)]
    return any(l) if (m-1) % 2 == 0 else all(l)

print(19, [s for s in range(1, 42+1) if f(s, 2)])
print(20, [s for s in range(1, 42+1) if not f(s, 1) and f(s, 3)])
print(21, [s for s in range(1, 42+1) if not f(s, 2) and f(s, 4)])
