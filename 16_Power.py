"""
// 面试题16：数值的整数次方
// 题目：实现函数double Power(double base, int exponent)，求base的exponent
// 次方。不得使用库函数，同时不需要考虑大数问题。
"""

def equal_zero(num):
    if abs(num - 0.0) < 0.0000001:
        return True

def power(base, exponent):
    """需要考虑正数、负数和0。浮点数不能直接用==比较"""
    if equal_zero(base) and exponent < 0:
        raise ZeroDivisionError

    ret = power_value(base, abs(exponent))
    if exponent < 0:
        return 1.0 / ret
    else:
        return ret

def power_value(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    ret = power_value(base, exponent >> 1)  # 使用右移代替除2
    ret *= ret
    # 使用位运算代替求余来判断奇偶
    if exponent & 0x1 == 1:
        ret *= base

    return ret

if __name__ == '__main__':
    print(power(3, 3))
    print(power(-2, -6))
