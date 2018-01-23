"""
// 面试题4：二维数组中的查找
// 题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按
// 照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个
// 整数，判断数组中是否含有该整数。
"""

def find(matrix, number):
    """
    思路：从左下角或者右上角开始比较
    :param matrix:
    :param number:
    :return:
    """
    if not matrix:
        return False

    rows, colums = len(matrix), len(matrix[0])

    row, colum = 0, colums - 1
    while row < rows - 1 and colum > 0:
        if number == matrix[row][colum]:
            print(number, row, colum)
            return True
        elif number > matrix[row][colum]:
            row += 1
        else:
            colum -= 1
    return False

if __name__ == "__main__":
    matrix = [[1, 2, 8, 9],
              [2, 4, 9, 12],
              [6, 8, 11, 15]]
    number = 8
    print(find(matrix, number))