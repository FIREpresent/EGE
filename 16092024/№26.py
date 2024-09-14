f = open('26_59852.txt', 'r')
lines = list(map(int, f.readlines()))
N = lines[0]
K = lines[1]
lines = lines[2:]
details = lines[:N]
containers = lines[N:]

count = 0
summ = 0
for i in range(N):
    for j in range(K):
        if details[i] <= containers[j]:
            count += 1
            summ += details[i]
            containers[j] -= details[i]
            break
print(summ, count)