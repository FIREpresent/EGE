def func(n):
    dl = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            dl.append(i)
            dl.append(n // i)
    return dl


count = 0
for j in range(800_000, 10 ** 6):
    d = func(j)
    if len(d) != 0:
        M = max(d) + min(d)
        if M % 10 == 4:
            print(j, M)
            count += 1
    if count == 5:
        break
