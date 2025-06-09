def f(a, b, m):
    if a + b >= 178:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a+4, b, m-1), f(a*2, b, m-1), f(a, b+3, m-1), f(a, b*3, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print([s for s in range(1, 156+1) if f(21, s, 2)])
print(sum([s for s in range(1, 156+1) if not f(21, s, 1) and f(21, s, 3)]))
print([s for s in range(1, 156+1) if not f(21, s, 1) and not f(21, s, 3) and f(21, s, 5)])