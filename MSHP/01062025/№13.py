from ipaddress import ip_network

v = []
c = 0
for ip_ in ip_network('135.221.128.0/255.255.128.0'):
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    v.append(str(bin_ip).count('1'))

print(min(v))