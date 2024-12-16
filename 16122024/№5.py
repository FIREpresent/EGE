# def func(x):
#     N = bin(x)[2:]
#     K = sum(list(map(int, str(N))))
#     N1 = N + str(bin(int(K) % 3)[2:])
#     K1 = sum(list(map(int, str(N1))))
#     N2 = N1 + str(bin(int(K1) % 5)[2:])
#     return int(N2, 2)
#
# s = set()
# for i in range(1_222_222_222, 1_555_555_661):
#     s.add(func(i))
#
# print(len(s))


print(int((bin(1555555666)[2:])[:-5], 2) - (int((bin(1222222222)[2:])[:-5], 2) + 1))