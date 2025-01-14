def F1(x, y):
    if x > y or x == 11:
        return 0
    if x == y:
        return 1
    return F1(x + 1, y) + F1(x * 2, y)

def F2(x, y):
    if x > y or x == 12:
        return 0
    if x == y:
        return 1
    return F2(x + 1, y) + F2(x * 2, y)
print(F1(2, 12) * F1(12, 24) + F2(2, 11) * F2(11, 24))