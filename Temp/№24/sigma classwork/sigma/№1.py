f = open('24-1 (12).txt')
s = f.read()
for x in '02468':
    s = s.replace(f'{x}', '+')
for y in '13579':
    s = s.replace(f'{y}', '-')
for _ in range(10_000):
    s = s.replace('+-', '+ -')
    s = s.replace('-+', '- +')
v = s.split(' ')
print(len(max(v, key=len)))

