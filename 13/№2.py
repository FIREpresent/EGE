from ipaddress import ip_network


c = 0
for ip_ in ip_network('184.178.54.144/255.255.255.240'):
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    if '111' in bin_ip:
        c += 1
print(c)