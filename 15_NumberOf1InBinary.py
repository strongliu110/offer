"""
// 面试题15：二进制中1的个数
// 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
// 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。
"""
import sys
import math

def numberOf1_1(num):
    """右移，存在负数左移问题"""
    count = 0
    while num:
        if num & 1:
            count += 1
        num = num >> 1
    return count

def numberOf1_2(num):
    """左移，循环次数等于二进制位数。32位数需要32次"""
    count = 0
    flag = 1
    while flag <= math.pow(2, 32):
        if num & flag:
            count += 1
        flag = flag << 1
    return count

# 把一个数-1，再和原数做与，会把该数最右边的1变为0
def numberOf1(num):
    count = 0
    while num:
        count += 1
        num = (num - 1) & num
    return count

if __name__ == "__main__":
    print(numberOf1_1(1024))
    print(numberOf1_2(1024))
    print(numberOf1(1024))

