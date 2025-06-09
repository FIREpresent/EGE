def f(x, y):
    if x > y or x == 58:
        return 0
    elif x == y:
        return 1
    return f(x+1, y) + f(x+2, y) + f(x+3, y) + f(x*4, y)

print(f(38, 45)*f(45,68))