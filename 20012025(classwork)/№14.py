num = 12**34 + 7*12**26 - 3*12**16 + 2*12**5 + 552
base = 12
letters = 'ABCDEF'
new = ''

while num > 0:
    num, remainder = divmod(num, base)
    if remainder > 9:
        letter_id = remainder - 10
        remainder = letters[letter_id]
    new = str(remainder) + new

print(len(set(list(new))))

