def f(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return f(n//2) + 3
        elif n % 2 != 0:
            return 2*f(n-1)+1


vec = []
for i in range(1, 1001):
    vec.append(f(i))

print(len(set(vec)))