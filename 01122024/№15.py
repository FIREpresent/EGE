for x in '1234567':
    for y in '01234567':
        num1, num2 = int(x + '01' + y + '4', 9), int(x + y + '544', 8)
        if (num1 + num2) % 89 == 0:
            print((num1 + num2) // 89)
            break