s = 'ABOPT'

count = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                count += 1
                if str(i+j+k+l) == 'TAPA':
                    print(count)
                    break