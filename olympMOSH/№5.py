n, k = map(int, input().split())
v = list(map(int, input().split()))
res = []
count = {}
uniq = set()

for i in range(k):
    nmb = v[i]
    count[nmb] = count.get(nmb, 0) + 1

for nmb, cnt in count.items():
    if cnt == 1:
        uniq.add(nmb)

for i in range(n - k + 1):
    if i > 0:
        d = v[i - 1]
        count[d] -= 1
        if count[d] == 1:
            uniq.add(d)
        elif count[d] == 0:
            del count[d]
        else:
            if d in uniq:
                uniq.remove(d)

        c = v[i + k - 1]
        count[c] = count.get(c, 0) + 1
        if count[c] == 1:
            uniq.add(c)
        else:
            if c in uniq:
                uniq.remove(c)

    if uniq:
        maximum = max(uniq)
    else:
        maximum = -1
    res.append(maximum)

print(*res)