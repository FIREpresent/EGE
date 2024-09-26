for x in range(174457, 174506):
    v = []
    for i in range(2, x-1):
        if x % i == 0:
            v.append(i)
    if len(v) == 2:
        print(v[0], v[1])
    v.clear()
