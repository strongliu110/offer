"""
// 面试题42：连续子数组的最大和
// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
"""

# 举例分析数组，累加比较
# 采用动态规划分析（实现一致）
def sub_max_sum(nums):
    if not nums:
        return None

    current_sum = 0
    max_sum = float("-inf")  # 负无穷
    for num in nums:
        if current_sum <= 0:
            current_sum = num
        else:
            current_sum += num
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == '__main__':
    test = [1, -2, 3, 10, -4, 7, 2, -5]
    print(sub_max_sum(test))