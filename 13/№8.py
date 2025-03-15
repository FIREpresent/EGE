from ipaddress import ip_network

c = 0
for ip_ in ip_network('140.19.96.0/255.255.248.0'): #ip address - X, mask - Y #all ips in network XXX
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    if bin_ip[:8].count('1') == bin_ip[8:16].count('1') == bin_ip[16:24].count('1') == bin_ip[24:].count('1'):
        c += 1
print(c)