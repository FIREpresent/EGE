from re import findall

s = '12345ffhfhfdkf012444jkfgjkgf+*431000012c12dd'

num = r'(?:0|(?:[1-9][0-9]*))'
l = findall(num, s)
print(l)
# ['12345', '0', '12444', '431000012', '12']

s = '12345+*+012444+*431000012+12*123'
num = r'(?:0|(?:[1-9][0-9]*))'
pat = rf'(?:{num}(?:[+*]{num})*)'
l = findall(pat, s)
print(l)
#['12345', '0', '12444', '431000012+12*123']