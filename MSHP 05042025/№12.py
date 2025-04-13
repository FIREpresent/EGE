s = '8'*18 + '5'*3

while '555' in s or '888' in s:
    if '555' in s:
        s = s.replace('555', '8')
    while '888' in s:
        s = s.replace('888', '5')
    if '555' in s:
        s = s.replace('555', '8')

print(s)
