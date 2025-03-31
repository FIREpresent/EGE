from ipaddress import ip_network


c = 0
for ip_ in ip_network('216.130.64.0/255.255.192.0'): #ip address - X, mask - Y #all ips in network XXX
    ip_new = list(map(int, str(ip_).split('.')))
    print(ip_new)
    if ip_new[0] % 2 == 0 and ip_new[1] % 2 == 0 and ip_new[2] % 2 == 0 and ip_new[3] % 2 == 0:
        c += 1
print(c)