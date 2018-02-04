"""
// 面试题45：把数组排成最小的数
// 题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼
// 接出的所有数字中最小的一个。例如输入数组{3, 32, 321}，则打印出这3个数
// 字能排成的最小数字321323。
"""

from functools import cmp_to_key

def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def mini(nums):
    if not nums:
        return

    sorted(nums, key=cmp_to_key(cmp))  # python3中cmp参数被废弃了
    return int(''.join([str(num) for num in nums]))

if __name__ == '__main__':
    test = [321, 32, 3]
    print(mini(test))