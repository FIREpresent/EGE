counter = 0
for A in range(0, 1000):
    flag = True
    for x in range(0, 500):
        for y in range(0, 500):
            k = ((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))
            if not(k):
                flag = False
                break
        if not(flag):
            break
    if flag:
        counter += 1

print(counter)

