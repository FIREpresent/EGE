from ipaddress import ip_network
count = 0
k = []
for ip_ in ip_network('94.159.76.0/255.255.255.128'):
    ip_bin = bin(int(ip_))[2:]
    k.append(ip_bin.count('0'))
    if ip_bin.count('0') == 10:
        print(ip_bin, ip_)
print(sorted(k))