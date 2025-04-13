from re import findall
with open('24-1.txt') as f:
    s = f.readline()
    pat = r'(?:[A-Z][1-9](?:[0-9])*[02468][A-Z])'
    l = findall(pat, s)
    max_ = -10**10
    for el in l:
        max_ = max(max_, int(el[1:-1]))
    print(max_)