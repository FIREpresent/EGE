def func(x):
    sum = ''
    while x:
        x //= 3
        sum += str(x % 3)
    return sum[::-1]

print(func(9**8 + 3**5 - 2).count('2'))