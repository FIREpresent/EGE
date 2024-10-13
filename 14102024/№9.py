count = 0
for a in range(1,9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(0, 9):
                for e in range(0, 9):
                    if a > b > c > d > e:
                        count += 1
print(count)