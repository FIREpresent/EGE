from ipaddress import ip_network


c = 0
for ip_ in ip_network('143.168.72.213/255.255.255.240', 0):
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])

print(c)