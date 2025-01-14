from ipaddress import *
net4 = list(ip_network('172.16.168.0/255.255.248.0',0))
summary = 0
counter = 0
for x in net4:
    summary += 1
    print (f"{bin(int(x))[2:]}, {x}, {summary}")

    s = bin(int(x))[2:]
    if s.count('1') % 5 != 0:
        counter += 1

print(counter)