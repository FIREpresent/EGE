from ipaddress import ip_network
count = 0
for ip_ in ip_network('202.75.38.176/255.255.255.240'):
    ip_bin = bin(int(ip_))[2:]
    if '000' not in ip_bin and '111' not in ip_bin:
        count += 1
print(count)