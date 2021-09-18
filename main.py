def enter_matrix():
    print('введите матрицу в формате: a11 a12 a13/a21 a22 a23/a31 a32 a33')
    matrix = [[int(x) for x in y.split()] for y in input().split('/')]
    return matrix

def track (matrix):
    track = 0
    for i in range(len(matrix)):
        track += matrix[i][i]
    return track
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2): return('Матрицы не совместимы')
    matrix_done = [[0 for x in range(len(y))] for y in matrix1]
    for y in range(len(matrix1)):
        for x in range(len(matrix1[1])):
            matrix_done[y][x] = matrix1[y][x] + matrix2[y][x]
    return matrix_done
def matrix_multiplication(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix2[0])
    p = len(matrix1[0])
    matrix_result = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                matrix_result[i][j] += matrix1[i][k]*matrix2[k][j]
    return matrix_result
def minor(matrix,k):
    minor = matrix[1:]
    for i in range(len(minor)):
        minor[i] = minor[i][:k] + minor[i][k+1:]
    print('             ', minor)
    return minor
def det (matrix):
    ans = 0
    if len(matrix[0]) == 1:
        return matrix[0][0]
    else:
        for k in range(len(matrix[0])):
            ans+= matrix[0][k]*det(minor(matrix, k))*(-1)**(2+k)
    return  ans
matrix1 = enter_matrix()
print(det(matrix1))