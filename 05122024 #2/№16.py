def F(n):
    if n >= 2000:
        return 2000
    else:
        if n % 2 != 0:
            return n * F(n + 1)
        else:
            return n * (F(n + 1)//2)
print(F(1998)//F(2001))