f = open('27_B.txt')
n = int(f.readline())
max_summ = 0
summ = 0
k = 43
prefix = [10 ** 10] * k
for i in range(n):
    x = int(f.readline())
    summ += x
    if summ % k == 0:
        max_summ = summ
    max_summ = max(max_summ, summ - prefix[summ % k])
    prefix[summ % k] = min(summ, prefix[summ % k])
print(max_summ)