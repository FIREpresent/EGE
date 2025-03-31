from ipaddress import ip_network
### 127 < 128 - 31 бита, тогда приписывать в bin_ip = '000' + bin(int(ip_))[2:]
### 63 < 63 30 бит дописать '000' + '000'
### 31 < 32 29 бит '000' + '000' + '000'

c = 0
for ip_ in ip_network('XXX.XXX.XXX.XXX/YYY.YYY.YYY.YYY'): #ip address - X, mask - Y #all ips in network XXX
    bin_ip = bin(int(ip_))[2:]
    print(ip_, bin(int(ip_))[2:])
    if bin_ip.count('1') == bin_ip.count('0'):
        c += 1
print(c)