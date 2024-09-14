arr = []
for i in ' 0123456789':
    for j in ' 0123456789':
            for l in ' 0123456789':
                for m in '0123456789':
                    if i == ' ' and j == ' ' and l == ' ':
                        s = '14022' + str(m) + '1'
                    elif i == ' ' and l == ' ':
                        s = '1' + str(j) + '4302' + str(m) + '1'
                    elif i == ' ' and j == ' ':
                        s = '1' + str(l) + '4302' + str(m) + '1'
                    elif j == ' ' and l == ' ':
                        s = '1' + str(i) + '4302' + str(m) + '1'
                    elif i == ' ':
                        s = '1' + str(j) + str(l) + '4302' + str(m) + '1'
                    elif j == ' ':
                        s = '1' + str(i) + str(l) + '4302' + str(m) + '1'
                    elif l == ' ':
                        s = '1' + str(i) + str(j) + '4302' + str(m) + '1'
                    else:
                        s = '1' + str(i) + str(j) + str(l) + '4302' + str(m) + '1'
                    if int(s) % 3147 == 0:
                        arr.append(int(s))

print(*sorted(list(set(arr))))