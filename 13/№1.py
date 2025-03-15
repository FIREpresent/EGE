from ipaddress import ip_network


c = 0
for ip_ in ip_network('192.168.248.176/255.255.255.240'):
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    if bin_ip.count('1') > bin_ip.count('0'):
        c += 1
print(c)