def func(num, base):
  s = ''
  while num:
    s += str(num % base)
    num //= base
  return int(s[::-1])

for x in range(1, 2030):
  if str(func(3**100 - x, 3)).count('0') == 2:
    print(x)
    break