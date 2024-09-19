s = 'AB9CH'
alphabet = '0123456789ABCDEFGHIJK'

summ = 0
s = list(s[::-1])
for i in range(len(s)):
    s[i] = alphabet.index(s[i])
    summ += s[i]*20**i
print(summ)

