
for num in range(2023, 10**10, 2023):
    if (str(num)[0] == '1') and (str(num)[2:6] == '2139') and (str(num)[-1] == '4'):
        print(num, num//2023)