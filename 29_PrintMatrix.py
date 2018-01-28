"""
// 面试题29：顺时针打印矩阵
// 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
"""

def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    start = 0
    ret = []
    while rows > start * 2 and cols > start * 2:
        print_circle(matrix, start, rows, cols, ret)
        start += 1

    print(ret)

def print_circle(matrix, start, rows, cols, ret):
    col = cols - 1 - start
    row = rows - 1 - start

    # left->right
    for c in range(start, col + 1):
        ret.append(matrix[start][c])
    # top->bottom
    if start < row:
        for r in range(start + 1, row + 1):
            ret.append(matrix[r][col])
    # right->left
    if start < row and start < col:
        for c in range(start, col)[::-1]:
            ret.append(matrix[row][c])
    # bottom->top
    if start < row and start + 1 < col:
        for r in range(start + 1, row)[::-1]:
            ret.append(matrix[r][start])

if __name__ == '__main__':
    mat = [[1, 2],
           [5, 6]]
    print_matrix(mat)