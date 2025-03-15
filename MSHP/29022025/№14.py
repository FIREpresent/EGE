def f(x, a):
    if x == a:
        return 1
    elif x > a:
        return 0
    return f(x+1, a) + f(x*2, a) + f(x*3, a)

print(f(2, 7)*f(7, 28))