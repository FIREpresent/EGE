
def func(x):
    while '111' in x:
        x = x.replace('111', '2', 1)
        x = x.replace('222', '11', 1)
    return x

print(func('1'*78))