# def func(num, base):
#   s = ''
#   while num:
#     s += str(num % base)
#     num //= base
#   return int(s[::-1])
s = '0123456789ABC'
v = []
for x in s:
  for y in s:
    if (int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18)) % 9 == 0:
        v.append(int(f'8{x}78{y}', 13) + int(f'79{x}{y}7', 18))

print(min(v) // 9)