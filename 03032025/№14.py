def func(num, base):
  s = ''
  while num:
    s += str(num % base)
    num //= base
  return int(s[::-1])

print(str(func(36**7 + 6**19 - 18, 6)).count('0'))