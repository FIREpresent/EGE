a=['О','А',]
b=['Р','С','М','Х']
count = 0
for b1 in a:
    for b2 in b:
        for b3 in a:
            for b4 in b:
                for b5 in a:
                    for b6 in b:
                        for b7 in a:
                            for b8 in b:
                                s = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8
                                if s.count('Р') == 1 and s.count('О') == 2 and s.count('С') == 1 and s.count('М') == 1 and s.count('А') == 2 and s.count('Х') == 1:
                                    count += 1

print(count*2)