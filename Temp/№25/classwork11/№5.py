def div(x):
    l = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    return sorted(list(l))

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

l = 0
for n in range(190_061, 190_072+1):
    k = div(n)
    nechet = [el for el in k if el % 2 != 0]
    if len(nechet) == 4:
        print(nechet[-1], nechet[-2])