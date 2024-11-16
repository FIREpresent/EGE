import sys

sys.setrecursionlimit(10000)
def F(n):
    if n < 15:
        return n
    elif n >= 15:
        return F(n % 15) * F(n // 15)

count = 0
for num in range(0, 3**40):
    if F(num) == 7560:
        count += 1
print(count)