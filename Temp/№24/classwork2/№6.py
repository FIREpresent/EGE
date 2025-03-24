alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maximum = -10**10
with open('24-7.txt') as f:
    s = f.readline()
    for n in 'BCD':
        s = s.replace(n, 'Y')
    for n in 'AO':
        s = s.replace(n, 'X')

    for i in range(len(s) - 1):
        st = ''
        for j in range(i, len(s)):
            st += s[j]
            if st.count('XX') > 0 or st.count('YY') > 0:
                maximum = max(maximum, st.count('YX'))
                break



print(maximum)