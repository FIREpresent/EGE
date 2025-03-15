def f(n, m):
    return n % m == 0

for A in range(0, 1001):
    flag = 1
    for x in range(0, 300):
      for y in range(0, 300):
          k = (75 != 2*x + 3*y) or (A > 3*x) or (A > 2*y)
          if not(k):
            flag = 0
            break
    if flag:
        print(A)
        break