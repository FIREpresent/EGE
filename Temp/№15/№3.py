def f(x, A, B, C):
    return (x in C) <= (((x in B) and (not(x in A))) <= (not(x in C)))

C = [i for i in range(78, 151+1)]
B = [i for i in range(54, 120+1)]
res = []
for Amin in range(1, 300):
    for Amax in range(Amin+1, 300):
        A = [i for i in range(Amin, Amax+1)]
        flag = 1
        for x in range(1, 300):
            if not f(x, A, B, C):
                flag = 0
                break
        if flag:
            res.append(Amax-Amin)

print(min(res))
