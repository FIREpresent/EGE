from re import findall

with open('24-9.txt') as f:
    s = f.readline()
    num = r'(?:0|(?:[1-9][0-9]*))'
    pat = rf'(?:{num}(?:[+*]{num})*)'
    l = findall(pat, s)
l.sort(key=len, reverse=True)

max_ = 0

for el in l[:10]:

    if max_ > len(el):
        break

    print(el)
    new_s = ''
    sp = el.split('+')
    for pd_str in sp:
        if eval(new_s + f'+{pd_str}') == 0:
            new_s += f'+{pd_str}'
            #print(new_s[1:])
            max_ = max(max_, len(new_s[1:]))
        else:
            new_s = ''
    #print('-'*100)
print(max_)