count = 0
maximum = -10**10
for elem in range(3201, 12877):
    if elem % 4 == 0 and elem % 7 != 0 and elem % 11 != 0 and elem % 13 != 0 and elem % 19 != 0:
        count += 1
        maximum = max(maximum, elem)

print(count, maximum)