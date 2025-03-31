def f(a, b, m):
    if a+b >= 77: return m % 2 == 0
    if m == 0:
        return 0
    k = [f(a+1,b, m-1), f(a*2,b,m-1), f(a,b+1, m-1), f(a,b*2,m-1)]
    return any(k) if (m-1)%2 == 0 else any(k)
    # return any(k) if (m-1)%2 == 0 else all(k)

print(19, [s for s in range(1, 69+1) if f(7, s, 2)])
print(19, [s for s in range(1, 69+1) if not f(7, s, 1) and f(7, s, 3)])
print(19, [s for s in range(1, 69+1) if not f(7, s, 2) and f(7, s, 4)])