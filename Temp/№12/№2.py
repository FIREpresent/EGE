s='112'*3+'1'*4
while '11' in s :
    if '112' in s:
        s=s.replace('112','6',1)
    else:
        s=s.replace('11','3',1)
print(s.count('6') * 6 + s.count('3') * 3)