# def fu(a,b,m):
#     if a+b>=74: return m%2==0
#     if m==0:return 0
#     h=[fu(a+1,b,m-1),fu(a*2,b,m-1),fu(a,b+1,m-1),fu(a,b*2,m-1)]
#     return any(h) if (m-1)%2==0 else all(h)
#
#
# print(20,[s for s in range(1,61+1) if not fu(9,s,1) and fu(9,s,3)])
# print(21,[s for s in range(1,61+1) if not fu(9,s,2) and fu(9,s,4)])

