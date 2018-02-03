"""
// 面试题43：从1到n整数中1出现的次数
// 题目：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。例如
// 输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。
"""

# 获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
# http://www.cnblogs.com/qiaojushuang/p/7780445.html

# 求整数n的位数
def get_digits(n):
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret

# 每个n位数中包含1的个数公式为： f(n) = 9 * f(n-1) + 10 ** (n-1)
def get_1_digits(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current

def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)

if __name__ == '__main__':
    test = 21345
    import time
    t = time.clock()
    print(get_1_nums(test))
    print(time.clock() - t)