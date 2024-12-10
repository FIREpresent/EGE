def fu(a,m):
    if a<=17: return m%2==0
    if m==0:return 0
    h=[fu(a-1,m-1),fu(a//3 if a % 3 == 0 else a-2,m-1),fu(a//5 if a % 5 == 0 else a-3,m-1)]
    return any(h) if (m-1)%2==0 else all(h)
    #return any(h)

print([s for s in range(18,10000+1) if fu(s,2)])






