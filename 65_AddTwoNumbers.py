"""
// 面试题65：不用加减乘除做加法
// 题目：写一个函数，求两个整数之和，要求在函数体内不得使用＋、－、×、÷
// 四则运算符号。
"""

# 使用位运算。不考虑进位时相加和异或的结果一样，进位相当于与运算再向左移动一位
# Python中大整数会自动处理，因此对carry需要加个判断
def bit_add(num1, num2):
    carry = 1
    while carry:
        sum = num1 ^ num2
        carry = 0xFFFFFFFF & (num1 & num2) << 1
        carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
        num1 = sum
        num2 = carry
    return num1

if __name__ == '__main__':
    a = 222
    b = -199
    print(bit_add(a, b))