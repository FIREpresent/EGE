from ipaddress import ip_network
count = 0
k = []
for ip_ in ip_network('83.152.64.0/255.255.224.0'):
    ip_bin = bin(int(ip_))[2:]
    print(ip_bin, ip_)
print(sorted(k))