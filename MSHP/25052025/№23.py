def f(x, y):
    if x > y or x == 15 or x == 35:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y) + f(x**2, y)

print(f(2, 20)*f(20, 60)*f(60, 100))
