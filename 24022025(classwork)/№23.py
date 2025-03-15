
for A in range(1_000, -1, -1):
    flag = 1
    for x in range(0, 300):
      for y in range(0, 300):
          k = (x + 2*y > 48) or (y > x) or (x + 3*y < A)
          if k == 0:
            flag = 0
    if not flag:
        print(A)
        break