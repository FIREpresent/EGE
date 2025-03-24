def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return f(n//2) - 2
        return f(n-1) + 2

count = 0
for n in range(1000):
    if f(n) == -2:
      count += 1
print(count)