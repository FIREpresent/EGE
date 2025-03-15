from ipaddress import ip_network

c = 0
for ip_ in ip_network('158.132.161.128/255.255.255.128'): #ip address - X, mask - Y #all ips in network XXX
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    if bin_ip[-1] == '1':
        c += 1
print(c)