from ipaddress import ip_network

def func(x):
    for n in range(1, 9):
        if x == 2**n - 1:
            return 1
    return 0

c = 0
for ip_ in ip_network('139.75.100.0/255.255.252.0'): #ip address - X, mask - Y #all ips in network XXX
    ip_new = list(map(int, str(ip_).split('.')))
    print(ip_new)
    if func(ip_new[3]):
        c += 1
print(c)