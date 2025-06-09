def f(a, b, m):
    if 26 >= a+b >= 20:
        return m%2 == 0
    elif a+b>26:
        return (m-1)%2 == 0
    if m == 0:
        return 0
    h = [f(a+4, b, m-1), f(a*2, b, m-1), f(a, b+4, m-1), f(a, b*2, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h)

print(19, [s for s in range(1, 19+1) if f(11, s, 2)])
print(20, [s for s in range(1, 19+1) if not f(11, s, 1) and f(11, s, 3)])
print(21, [s for s in range(1, 19+1) if not f(11, s, 2) and f(11, s, 4)])