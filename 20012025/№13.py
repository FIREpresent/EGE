from ipaddress import *
net4 = list(ip_network('218.194.82.148/255.255.255.192',0))
summary = 0
counter = 0
for x in net4:
    summary += 1
    print (f"{bin(int(x))[2:]}, {x}, {summary}")
