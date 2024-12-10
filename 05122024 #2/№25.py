num = 452_021
count = 0

while count < 5:
    num += 1
    for d in range(2, int(num ** 0.5) + 1):
        if num % d == 0:
            if (num / d + d) % 7 == 3:
                print(num, num // d + d)
                count += 1
            break