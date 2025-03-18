for x in range(0, 10):
  if (int(f'4C{x}4', 15) + int(f'{x}62A', 13)) % 121 == 0:
    print((int(f'4C{x}4', 15) + int(f'{x}62A', 13)) // 121)
    break