def сheck(A, B, N):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            s = 0
            for k in range(N):
                s += A[i][k] * B[k][j]
            res[i][j] = s % 2
    return res


def func(B, N):
    total = 1 << (N * N)
    for mask in range(total):
        A = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                index = i * N + j
                if (mask >> index) & 1:
                    A[i][j] = 1
        A2 = сheck(A, A, N)
        if A2 == B:
            return A
    return [[0] * N for _ in range(N)]

T = int(input())

matrixes = []

for _ in range(T):
    N = int(input())
    B = []
    for i in range(N):
        B.append(list(map(int, input().split())))
    matrixes.append(func(B, N))

for matrix in matrixes:
    for i in range(len(matrix)):
        print(*matrix[i])
    print()
