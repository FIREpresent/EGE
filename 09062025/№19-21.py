def f(a, m):
    if a <= 23:
        return m % 2 == 0
    if m == 0:
        return 0
    tab = [f(a-3, m-1), f(a-5, m-1), f(a//2 if a % 2 == 0 else a//2 + 1, m-1)]
    return any(tab) if (m-1) % 2 == 0 else all(tab)

print(19, [s for s in range(24, 2000) if f(s, 2)])
print(20, [s for s in range(24, 2000) if not f(s, 1) and f(s, 3)])
print(21, [s for s in range(24, 2000) if not f(s, 2) and f(s, 4)])