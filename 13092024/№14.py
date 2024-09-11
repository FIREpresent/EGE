for a in '0123456789ABC':
    num1, num2 = int('26' + a + '98', 13), int('4' + a + '296', 13)
    if (num1 + num2)%34 == 0:
        print(num1 + num2)
        break
