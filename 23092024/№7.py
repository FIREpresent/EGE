#def func(num):
#    for i in range(len(num)-1):
#        if int(num[i]) % 2 == 0 and int(num[i+1]) % 2 == 0:
#            return 0
#    return 1


#c = 0
#for x in range(int('10000000000', 8), int('100000000000', 8)):
#    if str(x).count('1') + str(x).count('3') + str(x).count('5') + str(x).count('7') == 3 and func(str(x)):
#        c += 1
#        print(c)
#print(c)

from itertools import product
s = product('НЧ', repeat = 11)
cnt1 = 0
cnt2 = 0
for i in s:
    p=''.join(i)
    if p.count('НН') == 0 and p.count('Н') == 3:
        if p[0] == 'Н':
            cnt1 += 1
        else:
            cnt2 += 1
print(4**11*cnt1 + 3*4**10*cnt2)
