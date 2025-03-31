import sys
sys.setrecursionlimit(100_000)

def f(n):
    if n == 0:
        return 0
    return f(n-1) + n

for i in range(1, 101):
    print(i, f(i), f(i)%3)

count = 0

for i in range(765432010, 1542613235):
    if i % 3 == 1:
        count += 1

print(count)