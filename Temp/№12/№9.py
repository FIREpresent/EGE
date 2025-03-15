vec = []
for n in range(101, 1_000):
    if n % 9 == 0:
        s0 = '5' * n
        s = s0
        while '25' in s or '35' in s or '555' in s:
            while '555' in s or '11' in s or '2' in s:
                if '555' in s:
                    s = s.replace('555', '1', 1)
                if '11' in s:
                    s = s.replace('11', '25', 1)
                if '2' in s:
                    s = s.replace('2', '5', 1)
        vec.append((s0, s))

maximum = -10 ** 10
minimal_pair = (0, 0)
for i in range(len(vec)):
    k = sum(list(map(int, list(vec[i][1]))))
    if k > maximum:
        minimal_pair = vec[i]
        maximum = k

print(len(minimal_pair[0]))
