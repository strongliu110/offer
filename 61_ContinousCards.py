"""
// 面试题61：扑克牌的顺子
// 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
// 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
"""

import random

# 先把数组排序；其次统计数组中0的个数；最后统计排序后的数组中相邻数字之间的空缺总数
def is_continus(nums, k):
    datas = [random.choice(nums) for _ in range(k)]

    datas.sort()
    print(datas)
    numberOfZero = datas.count(0)
    small = numberOfZero
    big = small + 1  # 因为排过序了，所以从0的后边开始
    numberOfGap = 0
    while big < k:
        if datas[small] == datas[big]:  # 两个数相等，有对子不可能是顺子
            return False

        numberOfGap += datas[big] - datas[small] - 1
        small = big
        big += 1
    if numberOfGap > numberOfZero:
        return False
    else:
        return True

if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            0, 0]
    print(is_continus(test, 5))