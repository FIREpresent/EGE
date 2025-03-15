s = '1'*81

while "00" not in s:
     s = s.replace("033", "21120", 1)
     s = s.replace("034", "21120", 1)
     s = s.replace("04", "220", 1)
     s = s.replace("030", "100", 1)


print(s)