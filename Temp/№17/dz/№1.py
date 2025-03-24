count = 0
maximum = -10**10
for elem in range(1512, 13202):
    if elem % 7 == 0 and elem % 11 != 0 and elem % 13 != 0 and elem % 17 != 0 and elem % 23 != 0:
        count += 1
        maximum = max(maximum, elem)

print(count, maximum)