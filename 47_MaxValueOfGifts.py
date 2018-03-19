"""
// 面试题47：礼物的最大价值
// 题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
// （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或
// 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
// 算你最多能拿到多少价值的礼物？
"""

import numpy

# 采用动态规划。f(i,j)=max(f(i-1,j),f(i,j-1))+a[i][j]
# 如果是第一行则：f(0,j)=f(0,j-1)+a[0][j]。如果是第一列则：f(i,0)=f(i-1,0)+a[i][0]。
def max_value(values):
    if not values:
        return None

    rows = len(values)
    cols = len(values[0])
    maxValue = numpy.zeros([rows, cols])
    for i in range(0, rows):  # 注意range[0, rows)
        for j in range(0, cols):
            if i == 0 and j == 0:  # 如果是第一行第一列
                maxValue[i][j] = values[i][j]
            elif i == 0:  # 如果是第一行
                maxValue[i][j] = maxValue[i][j-1] + values[i][j]
            elif j == 0:  # 如果是第一列
                maxValue[i][j] = maxValue[i-1][j] + values[i][j]
            else:
                maxValue[i][j] = max(maxValue[i-1][j], maxValue[i][j-1]) + values[i][j]

    return maxValue[rows-1][cols-1]

if __name__ == "__main__":
    values = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    print(max_value(values))  # 53
