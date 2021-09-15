def enter_matrix():
    print('введите матрицу в формате: a11 a12 a13/a21 a22 a23/ a31 a32 a33')
    matrix = [[int(x) for x in y.split()] for y in input().split('/')]
    return matrix

def track 