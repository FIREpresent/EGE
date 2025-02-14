def func(num, base):
  s = ''
  while num:
    s += str(num % base)
    num //= base
  return int(s[::-1])



n = str(func(125**5 + 25**9 - 30, 5))
print(n.count('4'))
