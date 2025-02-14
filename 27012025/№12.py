s = '1' * 99
while '111' in s:
    if '222' in s:
        s = s.replace('222', '1', 1)
    else:
        s = s.replace('111', '2', 1)
print(s)