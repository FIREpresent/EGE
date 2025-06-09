# for N in range(256):
#     N_x = bin(N)[2:]
#     N_bin = '0'*(8-len(N_x)) + N_x
#     count = 0
#     st = ''
#     for elem in N_bin[::-1]:
#         if elem == '1':
#             count += 1
#         if count > 1:
#             if elem == '0':
#                 st += '1'
#             else:
#                 st += '0'
#         else:
#             st += elem
#     st = st[::-1]
#
#     if int(st, 2) == 178:
#         print(N)
#         break

for number in range(256):
    binary_number = bin(number)[2:].zfill(8)
    new_bin = ''
    for i in range(len(binary_number)):
        if binary_number[i] == '1' and binary_number[i+1:].count('1') == 0:
            new_bin += binary_number[i:]
            break
        else:
            if binary_number[i] == '1':
                new_bin += '0'
            else:
                new_bin += '1'
    decimal_result = int(new_bin, 2)

    if decimal_result == 178:
        print(number)