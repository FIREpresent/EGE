def check(tr, m):
    cond1 = [999 < abs(x) < 10000 for x in tr]
    d13 = [abs(x) % 13 == 0 for x in tr]
    d7 = [abs(x) % 7 == 0 for x in tr]
    cond3 = [x > m for x in tr]

    return 0 < sum(cond1) < 3 and sum(d13) > sum(d7) and all(cond3)

n = [int(x) for x in open('17-5.txt')]

n151 = [x for x in n if abs(x) % 1000 == 151]
m = sum(n151) / len(n151)

min_sum = 10**10
q = 0

for tr in zip(n, n[1:], n[2:]):
    if check(tr, m):
        q += 1
        min_sum = min(min_sum, sum(tr))

print(q, min_sum)