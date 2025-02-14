s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = s[:25]
for x in s[::-1]:
  if (int(f'11353{x}12', 25) + int(f'135{x}21', 25)) % 24  ==  0:
    print((int(f'11353{x}12', 25) + int(f'135{x}21', 25)) // 24)
    break