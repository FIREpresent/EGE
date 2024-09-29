
count = 0
for num in range(2422000, 2422080 + 1):
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            break
    else:
        count += 1
        print(count, num)