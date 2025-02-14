from itertools import count

maximum_d_count = 0
minimum_num = 10**10
for num in range(568_023, 569_231):
    count = 0
    for d in range(1, num+1):
        if num % d == 0:
            count += 1
    maximum_d_count = max(maximum_d_count, count)

for num in range(568_023, 569_231):
    count = 0
    for d in range(1, num+1):
        if num % d == 0:
            count += 1

    if maximum_d_count == count:
        minimum_num = min(minimum_num, num)


print(maximum_d_count, minimum_num)
