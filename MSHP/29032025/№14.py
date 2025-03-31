def func(num, base):
  while not (2 <= base <= 36):
    base = int(input('Основание (2-36): '))

  new = ''

  while num > 0:
    num, remainder = divmod(num, base)
    if remainder > 9:
      letter = remainder - 10
      remainder = chr(ord('A') + letter)
    new = str(remainder) + new

  return new

print(len(set(list(str(func(3*11**58 + 15*11**55-99*11**18 + 125*11**9 + 381, 11))))))