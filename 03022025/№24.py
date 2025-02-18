f = open('24.txt').readline()
k = 1
m = 0
for i in range(len(f)-1):
    if f[i] == 'B' and f[i+1] == 'B':
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)