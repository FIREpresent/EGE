from ipaddress import ip_network
count = 0
k = []
for ip_ in ip_network('124.8.0.0/255.248.0.0'):
    ip_bin = bin(int(ip_))[2:]
    k.append(ip_bin.count('0'))
print(max(k))