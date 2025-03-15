from ipaddress import ip_network


for num in range(0, 256):
    A = num
    flag = 1
    c = 0
    for ip_ in ip_network('64.129.'+str(A)+'.10/255.255.252.0', False):
        bin_ip = bin(int(ip_))[2:]
        # print(ip_, bin(int(ip_))[2:])
        if bin_ip[:16].count('1') > bin_ip[16:].count('1'):
            flag = 0

    if flag:
        print(A)
        break