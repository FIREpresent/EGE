from re import findall
with open('24.txt') as f:
    s = f.readline()
    s = s.replace('A', 'Y').replace('E', 'Y').replace('O', 'Y')
    s = s.replace('B', 'X').replace('C', 'X').replace('D', 'X').replace('F', 'X')
    pat = r'(?:XXY)+'
    v = findall(pat, s)
    print(v)

print(sorted(v, key=len))
print(len('XXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXYXXY'))