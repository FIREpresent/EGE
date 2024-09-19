for A in range(100):
    count = 0
    for x in range(100):
        for y in range(100):
            if (3 * x + 5 * y < A) or (x >= y) or (y > 8):
                count += 1

    if count == 10000:
        print(A)
        break