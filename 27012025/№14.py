def func(num, base):
  s = ''
  while num:
    s += str(num % base)
    num //= base
  return int(s[::-1])

print(str(func(36**8 + 6**20 - 12, 6)).count('5'))