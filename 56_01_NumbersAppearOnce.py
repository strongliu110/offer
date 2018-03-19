"""
// 面试题56（一）：数组中只出现一次的两个数字
// 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
// 找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""

# 按位异或，在得到的值中找到为1的某位，然后把数组按照该位是0还是1分为两组
def only_once_number(nums):
    if not nums:
        return None

    tmp = 0
    for num in nums:  # 获取两个值的异或结果
        tmp ^= num

    print(tmp)
    index = first_bit1(tmp)  # 为1的某位
    ret1, ret2 = 0, 0
    for num in nums:
        if is_bit1(num, index):
            ret1 ^= num
        else:
            ret2 ^= num
    return [ret1, ret2]


def first_bit1(num):
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret

def is_bit1(num, index):
    num = num >> index
    return num & 1

if __name__ == "__main__":
    test = [1, 2, 3, 4, 3, 1, -1, -1]
    print(only_once_number(test))