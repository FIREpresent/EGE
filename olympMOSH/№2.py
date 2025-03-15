def matrix_square_mod2(A):
    """
    Возвращает квадрат матрицы A в поле mod 2:
    B = A^2, где B[i][j] = sum(A[i][k]*A[k][j]) % 2
    """
    n = len(A)
    B = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += A[i][k] * A[k][j]
            B[i][j] = s % 2
    return B


def find_square_root(B):
    """
    Перебирает все 0-1 матрицы A размера N x N
    и ищет любую A, удовлетворя B = A^2 (mod 2).
    Если не найдено, возвращает None.
    """
    n = len(B)
    total_variants = 1 << (n * n)  # 2^(n*n)

    for mask in range(total_variants):
        # Собираем матрицу A из битов mask
        A = [[0] * n for _ in range(n)]
        bit_index = 0
        for i in range(n):
            for j in range(n):
                A[i][j] = (mask >> bit_index) & 1
                bit_index += 1

        # Считаем A^2 mod 2
        A_sq = matrix_square_mod2(A)
        if A_sq == B:
            return A
    return None

N = int(input())

B = []
for i in range(N):
    B.append(list(map(int, input().split())))

print(find_square_root(B))

N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = [[0 for j in range(N)] for i in range(N)]

print(B)

for i in range(N):
    for j in range(N):
        B[i][j] = sum([A[i][k] * A[k][j] for k in range(N)]) % 2
print(B)

