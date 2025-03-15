s25 = 0
a = 0
while s25 != 48:
    a += 1
    s = '1'*15 + a*'2'
    while '12' in s :
        s=s.replace('12','',1)
        s=s +'4'
        s25 = s.count('1')+s.count('2')*2+s.count('4')*4
print(a)