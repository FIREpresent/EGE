for num in range(210235,210301):
    v = []
    for d in range(2, int(num * 0.5) + 1):
        if num % d == 0:
            v.append(d)
        if len(v) > 4:
            break
    if len(v) == 4:
        print(*v)