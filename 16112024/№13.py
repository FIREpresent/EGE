for x in '01234567':
  for y in '1234567':
     if (int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)) % 117 == 0:
        print((int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)) // 117)