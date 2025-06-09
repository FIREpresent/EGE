for n in range(4, 1000+1):
    s = '>' + '0'*25 + '1'*n + '2'*25

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    m = sum(list(map(int, list(s.replace('>', '0')))))
    if len(str(m)) == 4 and m % 15 == 0:
        print(n)
        break