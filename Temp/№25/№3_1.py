from fnmatch import fnmatch

def div(x):
    l = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            l.add(i)
            l.add(x // i)
    return sorted(list(l))

vec1 = []
vec2 = []
for i in range(0, 10 ** 7 + 1, 217):
    if fnmatch(str(i), '14?4*'):
        vec1.append(i)
        vec2.append(sum([el for el in div(i) if el % 2 != 0]))

vec1 = vec1[::-1]
vec2 = vec2[::-1]
vec = []

for i in range(7):
    vec.append((vec1[i], vec2[i]))

for elem in vec[::-1]:
    print(*elem)


# 1494913 6889
# 1494696 6888
# 1494479 6887
# 1494262 6886
# 1494045 6885
# 1484931 6843
# 1484714 6842