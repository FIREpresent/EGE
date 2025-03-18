for x in range(0, 100):
    for y in range(0, 100):
        for z in range(0, 100):
            s = '0' + '1'*x + '2'*y + '3'*z + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(x+y+z+2)
                break