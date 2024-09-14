def func(min):
    for i in range(1,100):
        for j in range(1,100):
            if j > i and all((( 17 < x < 54) <= (((37 < x < 83) and not(i < x < j)) <= ( not(17 < x < 54)))) for x in range (1,100)):
                if j - i < min:
                    min = j - i

    return min

min = 1000
print(func(min))