"""
// 面试题64：求1+2+…+n
// 题目：求1+2+…+n，要求不能使用乘除法、for、while、if、else、switch、case
// 等关键字及条件判断语句（A?B:C）。
"""

from functools import reduce

def get_sum1(n):
    return sum(range(1, n+1))

def get_sum2(n):
    return reduce(lambda x, y: x+y, range(1, n+1))

if __name__ == '__main__':
    print(get_sum1(4))
    print(get_sum2(40))
