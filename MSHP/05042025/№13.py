from ipaddress import ip_network


c = 0
for ip_ in ip_network('216.130.64.0/255.255.192.0'):
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    v = str(ip_).split('.')
    if int(v[0]) % 2 == 0 and int(v[1]) % 2 == 0 and int(v[2]) % 2 == 0 and int(v[3]) % 2 == 0:
        c += 1

print(c)