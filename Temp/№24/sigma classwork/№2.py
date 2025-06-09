s = open('24-2.txt').read()
sp = s.split('T')
mx = 0
for i in range(len(sp) - 100):
    p = 'T'.join(sp[i:i+101])
    mx = max(mx, len(p))
print(mx)
