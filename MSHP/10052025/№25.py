def div(x):
    l = set()
    for d in range(1, int(x**0.5) + 1):
        if x % d == 0:
            l.add(d)
            l.add(x // d)
    return sorted(list(l))

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

v = []
l = 0
for n in range(586132, 586430+1):
    k = div(n)
    v.append([n, len(k)])

v = sorted(v, key=lambda x: x[1], reverse=True)
print(max(v[:3], key=lambda x: x[0]), min(v[:3]), v[:3])

#[586320, 80] [586224, 80]

print(div(586224))
# 80 293160
# 80 293112