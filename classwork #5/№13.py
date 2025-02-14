f = open('27-B_1.txt')
K = int(f.readline())
v = [int(line.strip()) for line in f.readlines()]


# ans = set()
maxi = -10**10
maximum = -10**10
for i in range(len(v)):
    if (v[i] + 3*K) in v:
        # ans.add(v[i] + 3*K)
        # ans.add(v[i])
        maximum = max(v[i] + 3*K + v[i], maximum)
    if (v[i] - 3*K) in v:
        maximum = max(v[i] - 3*K + v[i], maximum)
    maxi = max(maxi, v[i])

print(maxi + maximum)
