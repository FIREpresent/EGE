M = [i for i in range(32, 68+1)]
N = [i for i in range(54, 76+1)]

def f(x, A, M, N):
    return (not((x in M) or (x in N))) == (not(x in A))

res = []
for Amin in range(1, 300):
    for Amax in range(Amin+1, 300):
        A = [i for i in range(Amin, Amax+1)]
        flag = 1
        for x in range(1, 4000):
            if not f(x*0.25, A, M, N):
                flag = 0
                break
        if flag:
            res.append(Amax-Amin)

print(min(res))
