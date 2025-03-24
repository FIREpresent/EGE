for n in range(50, 250):
    flag = 1
    s = '0' + '1'*100 + '2' * n + '0'
    while '00' in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('012', '30', 1)
        s = s.replace('010', '00', 1)
    num = int(s)
    for d in range(2, int(num**0.5) + 1):
        if num % d == 0:
            flag = 0
            break
    if flag:
        print(n)
        break
