from re import findall

s = 'ZDROZDDROHDGYFEZAROZEROZUROZRRO'
pat = r'(?:Z[A-Z]RO)+'
# * - повторение части от нуля и больше
# + - повторение части от единицы и больше
#[^U] - кроме U
#[A-Z^U] - от A до Z включительно и без U
l = findall(pat, s)
print(l)