D = [i for i in range(7, 68+1)]
C = [i for i in range(29, 100+1)]

def f(x, A, D, C):
    return (x in D) <= (((not(x in C)) and (not(x in A))) <= (not(x in D)))

res = []
for Amin in range(1, 300):
    for Amax in range(Amin+1, 300):
        A = [i for i in range(Amin, Amax+1)]
        flag = 1
        for x in range(1, 6000):
            if not f(x*0.25, A, D, C):
                flag = 0
                break
        if flag:
            res.append(Amax-Amin)

print(min(res))