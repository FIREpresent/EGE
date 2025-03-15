vec = []
for n in range(100, 1000):
    s0 = '1'*n
    s = s0
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('2222', '333', 1)
        s = s.replace('33', '1', 1)
    vec.append((s0, s))

minimum = 10**10
minimal_pair = (0, 0)
for i in range(len(vec)):
    k = vec[i][1].count('1')
    print(k)
    if k < minimum:
        minimal_pair = vec[i]
        minimum = vec[i][1].count('1')

print(len(minimal_pair[0]))