from fnmatch import fnmatch
def func(x, base):
    v = []
    while x:
        v.append(int(x % base))
        x = x // base
    return v[::-1]

for i in range(0, 2*10**9 + 1):
    s = func(i, 7)
    if fnmatch(str(i), '1*586?6') and s == s[::-1]:
        print(i, sum(s))