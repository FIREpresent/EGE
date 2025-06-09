from ipaddress import *

for ip_ in ip_network('98.71.254.171/255.248.0.0', strict=False):
    ip_str = str(ip_)
    if ip_str.split('.')[-1] != '255':
        ip_bin = bin(int(ip_))[2:]
        if ip_bin.count('1') % 7 == 0:
            print(ip_str)
            break