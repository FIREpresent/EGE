f = open("demo_2025_9.csv")
ans = 0
for i in f:
    l = [int(x) for x in i.strip().split(',')]
    l1 = [x for x in l if l.count(x) == 3]
    l2 = [x for x in l if l.count(x) == 1]
    f1 = len(l1) == 3 and len(l2) == 3
    f2 = (sum(l1))**2 > (sum(l2))**2
    if f1 and f2:
        ans += 1

f.close()
print(ans)