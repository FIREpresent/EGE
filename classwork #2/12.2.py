count = 0
s = '01234567'
for x1 in s:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                for x5 in s:
                    if (x1 + x2 + x3 + x4 + x5).count('6') == 1:
                        num = '1357'
                        if (num.count(x1) and x2 == '6') == 0 and (num.count(x2) and x3 == '6') == 0 and (num.count(x3) and x4 == '6') == 0 and (num.count(x4) and x5 == '6') == 0:
                            if (x4 == '6' and num.count(x5)) == 0 and (x3 == '6' and num.count(x4)) == 0 and (x2 == '6' and num.count(x3)) == 0 and (x1 == '6' and num.count(x2)) == 0:
                                if x1 != '0':
                                    count += 1
print(count)
