
f = open('17.txt')
vec = [int(i) for i in f]

count = 0
maximum_sum  = -1*10**10

for i in range(len(vec)):
    for j in range(i+1, len(vec)):
        if i == j:
            continue
        if abs((vec[i] - vec[j])) % 2 == 0 and (vec[i] % 31 == 0 or vec[j] % 31 == 0) and vec[i] != vec[j]:
            count += 1
            maximum_sum = max(maximum_sum, vec[i] + vec[j])

print(count, maximum_sum)
