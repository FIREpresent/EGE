C = [i for i in range(48, 94+1)]
J = [i for i in range(83, 100+1)]

def f(x, A, C, J):
    return (not((x in C) or (x in J))) <= (not(x in A))

res = []

for Amin in range(1, 300):
    for Amax in range(Amin+1, 300):
        A = [i for i in range(Amin, Amax+1)]
        flag = 1
        for x in range(1, 300):
            if not f(x, A, C, J):
                flag = 0
                break
        if flag:
            res.append(Amax-Amin)

print(max(res))