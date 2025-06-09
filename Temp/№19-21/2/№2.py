def f(a, b, m):
    if a < 10 and b >= 10 or b < 10 and a >= 10:
        return m%2 == 0
    if m == 0:
        return 0
    h = [f(a-1, b, m-1), f(a-3, b, m-1), f(a, b-1, m-1), f(a, b-3, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print(19, [s for s in range(1, 1000+1) if f(s, s, 2)])
print(20, [s for s in range(10, 1000+1) if not f(13, s, 1) and f(13, s, 3)])
print(21, [s for s in range(10, 1000+1) if not f(13, s, 2) and f(13, s, 4)])