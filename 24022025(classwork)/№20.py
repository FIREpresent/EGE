s = '0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
s = sorted(s)
for a in s[:22]:
  if (int(f'63{a}59685', 22) + int(f'17{a}53', 22) + int(f'36{a}5', 22)) % 21 == 0:
    print((int(f'63{a}59685', 22) + int(f'17{a}53', 22) + int(f'36{a}5', 22)) // 21)
    break