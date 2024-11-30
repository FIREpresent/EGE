

for i in range(0, 30):
    for j in range(0, 30):
        for k in range(0, 30):
            x = '0' + '1'*i + '2'*j + '3'*k + '0'
            while '00' not in x:
                x = x.replace('01', '220', 1)
                x = x.replace('02', '1013', 1)
                x = x.replace('03', '120', 1)
            if x.count('1') == 13 and x.count('2') == 18:
                print(i+j+k+2)
                break


#
# A = []
# for x in range(20,-1,-1):
#     for y in range(20,-1,-1):
#         for z in range(20,-1,-1):
#             num = '0' + '1'*x + '2'*y + '3'*z +'0'
#             while '00' not in num:
#                 num = num.replace('01','220',1)
#                 num = num.replace('02','1013',1)
#                 num = num.replace('03','120',1)
#             if num.count('1') == 13 and num.count('2') == 18:
#                 print(x + y + z)
# print(min(A) + 2)