from ipaddress import *

c = 0
for ip_ in ip_network('192.168.248.176/255.255.255.240'):
    s = bin(int(ip_))[2:]
    if s.count('1') > s.count('0'):
        c += 1

print(c)