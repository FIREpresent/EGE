def f(a, m):
    if a >= 88: return m % 2 == 0
    if m == 0:
        return 0
    k = [f(a+1, m-1), f(a+4,m-1), f(a*3, m-1)]
    return any(k) if (m-1)%2 == 0 else all(k)
    # return any(k) if (m-1)%2 == 0 else all(k)

print(19, [s for s in range(1, 87+1) if f(s, 2)])
print(19, [s for s in range(1, 87+1) if not f(s, 1) and f(s, 3)])
print(19, [s for s in range(1, 87+1) if not f(s, 2) and f(s, 4)])