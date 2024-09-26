
def func(x):
    while '133' in x or '881' in x:
        if '133' in x:
            x = x.replace('133', '81', 1)
        else:
            x = x.replace('881', '13', 1)
    return x

s = '8' * 99 + '1'
print(func(s))