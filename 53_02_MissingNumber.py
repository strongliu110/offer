"""
// 面试题53（二）：0到n-1中缺失的数字
// 题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字
// 都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组
// 中，请找出这个数字。
"""

# 二分查找。问题可转换为在排序数组中找出第一个值和下标不相等的元素
def missing_number(nums):
    if not nums:
        return None

    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) >> 1  #右移效率更高
        if nums[mid] != mid:
            if (mid == 0) or (nums[mid - 1] == mid - 1):  # 中间数是第一个或中间数前一个等于下标
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":
    print(missing_number([0, 1, 2, 4, 5]))