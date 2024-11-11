def deliteli(n):
    deliteli = []
    for i in range(2, int(n, 0.5) + 1):
        if n % i == 0:
            deliteli.append(i)
            deliteli.append(n // i)
    return deliteli
count = 0
for j in range(800_000, 10, 6):
    d = deliteli(j)
    if len(d) != 0:
        M = max(d) + min(d)
        if M % 10 == 4:
            print(j, M)
            count += 1
        if count == 5:
            break