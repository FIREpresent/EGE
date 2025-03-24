alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maximum = -10**10
with open('24-5.txt') as f:
    s = f.readline()
    for i in range(len(s) - 1):
        st = ''
        for j in range(i, len(s)):
            st += s[j]
            if st.count('.') > 2:
                maximum = max(maximum, len(st)-1)
                break

print(maximum)




