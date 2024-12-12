for num in range(10_000, 1000, -1):

    v = list(map(int, list(str(num))))
    sum1 = v[0] + v[1]
    sum2 = v[1] + v[2]
    sum3 = v[2] + v[3]
    summ = sum1 + sum2 + sum3
    if str(summ - max(sum1, sum2, sum3) - min(sum1, sum2, sum3)) + str(max(sum1, sum2, sum3)) == '1215':
        print(num)
        break