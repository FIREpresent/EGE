f = open('26-1 (4).txt')
k = int(f.readline())
n = int(f.readline())
a = sorted([list(map(int, i.split())) for i in f])
count  = 0
maxt = kposled = 0
for i in range (1, k+1):
    start = 0
    for x in a:
        if x[0]-start >= 1 and x[0] > 0 and x[1] > 0:
            count +=1
            start = x[1]
            if x[0] > maxt:
                maxt = x[0]
                kposled = i
            x[0] = -1
            x[1] = -1
print(count, kposled)