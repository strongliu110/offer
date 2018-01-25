"""
// 面试题14：剪绳子
// 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
// 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
// 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
// 时得到最大的乘积18。
"""

import math

# 动态规划
# def maxProduct1(length):

# 贪婪算法
def maxProduct2(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    # ≥5时,尽可能的分为3
    timesOf3 = length // 3
    if length - timesOf3 * 3 == 1:
        timesOf3 -= 1

    # 2*2 > 3*1
    timesOf2 = (length - timesOf3 * 3) / 2

    return int(math.pow(3, timesOf3) * math.pow(2, timesOf2))  # 注意int()

if __name__ == "__main__":
    print(maxProduct2(5))
    print(maxProduct2(6))