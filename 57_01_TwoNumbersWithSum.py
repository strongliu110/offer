"""
// 面试题57（一）：和为s的两个数字
// 题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们
// 的和正好是s。如果有多对数字的和等于s，输出任意一对即可。
"""

# 定义两个指针找
def find_numbers_with_sum(nums, sum):
    if not nums:
        return None

    start = 0
    end = len(nums) - 1
    while start < end:
        current = nums[start] + nums[end]
        if current < sum:
            start += 1
        elif current > sum:
            end -= 1
        else:
            return nums[start], nums[end]
    return None

if __name__ == "__main__":
    test = [1, 2, 4, 7, 11, 15]
    print(find_numbers_with_sum(test, 15))
