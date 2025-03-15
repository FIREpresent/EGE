M = [int(x) for x in open('17_1.txt')]
maxi = max(M)
mini = min(M)
count = 0
otv = -9999999999
for i in range(len(M)-1):
    if (M[i] % 3 == mini % 3) or (M[i + 1] % 3 == mini % 3):
        if (M[i] % 7 == maxi % 7) or (M[i + 1] % 7 == maxi % 7):
                count += 1
                otv = max(otv, M[i] + M[i+1])
print(count, otv)