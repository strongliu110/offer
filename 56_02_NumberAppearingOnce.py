"""
// 面试题56（二）：数组中唯一只出现一次的数字
// 题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
// 找出那个只出现一次的数字。
"""

# 时间O(n)。若用排序后查找时间O(nlogn)，若用哈希记录次数空间O(n)
def apperaring_once(nums):
    if not nums:
        return None

    bit_sum = {}
    for num in nums:
        bit_mask = 1
        for j in reversed(range(0, 32)):  # 反向遍历
            bit = num & bit_mask
            if bit != 0:
                bit_sum[j] = bit_sum[j] + 1 if j in bit_sum else 1  # 为1的位的总数
                bit_mask = bit_mask << 1

    result = 0
    for i in range(0, 32):
        result = result << 1
        if i in bit_sum:
            result += bit_sum[i] % 3
        else:
            pass
    return result

if __name__ == "__main__":
    numbers = [1, 1, 2, 3, 2, 1, 2]
    print(apperaring_once(numbers))