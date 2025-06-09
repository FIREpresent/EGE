# def f(x, a1, a2):
#     B = (66 <= x <= 75)
#     C = (71 <= x <= 85)
#     A = (a1 <= x <= a2)
#     return (not A) <= (B == C)
#
# r = []
# d = [y for x in (66, 71, 75, 85) for y in (x, x + 0.1, x - 0.1)]
# for a1 in d:
#     for a2 in d:
#         if a2 >= a1 and all(f(x, a1, a2) for x in d):
#             r.append(a2-a1)
#
# print(round(max(r)))


def f(x):
    B = (36 <= x <= 75)
    C = (60 <= x <= 110)
    A = (a1 <= x <= a2)
    return (not A) <= (B == C)

r = []
d = [y for x in (36, 60, 75, 110) for y in (x, x + 0.1, x - 0.1)]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            r.append(a2-a1)

print(round(max(r)))

