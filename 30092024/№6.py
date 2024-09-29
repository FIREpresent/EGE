v = []
for i in range(1, 100):
    bin_num = bin(i)[2:]

    if i % 2 == 0:
        bin_num+= "10"
    else:
        bin_num += "01"
    new_num = int(bin_num, 2)
    if new_num <= 102:
        v.append(new_num)

print(max(v))