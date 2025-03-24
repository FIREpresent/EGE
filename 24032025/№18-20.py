def f(a, m):
    if a >= 63: return m % 2 == 0
    if m == 0:
        return 0
    k = [f(a+1, m-1), f(a+4, m-1), f(a*5, m-1)]
    # return any(k) if (m-1)%2 == 0 else any(k)
    return any(k) if (m-1)%2 == 0 else all(k)

print(19, [s for s in range(1, 62+1) if f(s, 2)])
print(19, [s for s in range(1, 62+1) if not f(s, 1) and f(s, 3)])
print(19, [s for s in range(1, 62+1) if not f(s, 2) and f(s, 4)])