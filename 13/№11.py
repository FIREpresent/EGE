from ipaddress import ip_network


for num in range(0, 9):
    A = int('1'*num + '0'*(8-num), 2)
    flag = 1
    c = 0
    for ip_ in ip_network('199.59.129.3/255.255.' + str(A) + '.0', False):
        bin_ip = bin(int(ip_))[2:]
        # print(ip_, bin(int(ip_))[2:])
        if bin_ip[:16].count('1') < bin_ip[16:].count('1'):
            flag = 0

    if flag:
        print(A)
        break