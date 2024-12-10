for x in '123456789AB':
    for y in '0123456789AB':
        s1 = int(x + '231' + y, 12)
        s2 = int('78' + x + '98' + y, 14)
        s = s1 + s2
        if s % 99 == 0:
            print(s // 99)
            break