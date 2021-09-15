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
matrix1 = [[1,2,3],[1,2,3],[1,2,3]]
matrix2 = [[4,5,6],[4,5,6],[4,5,6]]

print(matrix_addition(matrix1,matrix2))