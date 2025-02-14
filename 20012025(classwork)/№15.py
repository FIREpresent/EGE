def f(n, m):
    return n % m == 0

for A in range(0, 1001):
    flag = 1
    for x in range(0, 300):
      for y in range(0, 300):
          k = (x*y < A) or (y > x) or (x >= 8)
          if not(k):
            flag = 0
            break
    if flag:
        print(A)
        break