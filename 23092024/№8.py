k = 0
for a in range(1, 9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                for f in range(9):
                    s = str(a) + str(b) + str(c) + str(d) + str(f)
                    if s.count('5') == 1:
                        for i in range(len(s)):
                            if 0 < i < 4 and s[i] == '5':
                                if int(s[i-1]) % 2 == 0 and int(s[i+1]) % 2 == 0:
                                    k += 1
                                    break
                            elif i == 0 and s[i] == '5':
                                if int(s[i+1]) % 2 == 0:
                                    k += 1
                                    break
                            elif i == 4 and s[i] == '5':
                                if int(s[i-1]) % 2 == 0:
                                    k += 1
                                    break

print(k)
