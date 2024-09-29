

res = 0
for a in 'ЗИМА':
    for b in 'ЗИМА':
        for c in 'ЗИМА':
            for d in 'ЗИМА':
                for e in 'ЗИМА':
                    s = a + b + c + d + e
                    if (s.count('А') == 0 and s.count('И') == 1) or (s.count('А') == 1 and s.count('И') == 0):
                        res += 1
print(res)