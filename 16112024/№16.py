count = 0
maximum = -1
M = [int(x) for x in open('17.txt')]
max_el = max(M)
min_el = min(M)

for i in range(len(M)-1):
    if ((M[i] % 3 == min_el % 3) or (M[i + 1] % 3 == min_el % 3)) and ((M[i] % 7 == max_el % 7) or (M[i + 1] % 7 == max_el % 7)):
           count += 1
           maximum = max(maximum, M[i] + M[i + 1])
print(count, maximum)