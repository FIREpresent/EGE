for n in range (1, 300):
    s = '1' * n
    while '111' in s:
            s = s.replace('111', '2', 1)
            s = s.replace('222', '11', 1)
            s = s.replace('1', '2', 1)
    if len(s) == 3:
        print(f'{n:} is {s:}')

#221 211 222 212 211 222 212 211 222 212 211 222 212 211 222 212