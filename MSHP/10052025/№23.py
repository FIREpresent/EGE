def f(x, y, k):
    if x > y or x == 30 or x == 40 or k == 2:
        return 0
    elif x == y:
        return 1
    return f(x+1, y, 0) + f(x+3, y, 0) + f(x*2, y, k+1)

print(f(3, 20, 0)*f(20,60, 0))