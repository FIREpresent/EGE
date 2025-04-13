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

vec = []
for n in range(2532000, 2532160):
    if is_prime(n) and n % 10 == 7:
       vec.append(n)

for i in range(len(vec)):
    print(vec[i])