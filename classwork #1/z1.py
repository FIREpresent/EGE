def func5(x):
    num = ''
    while x:
        num += str(x % 5)
        x = x // 5
    print(int(num[::-1]))

func5(int(input()))