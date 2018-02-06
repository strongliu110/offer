"""
// 面试题53（三）：数组中数值和下标相等的元素
// 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
// 现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组{-3, -1,
// 1, 3, 5}中，数字3和它的下标相等。
"""

def num_equal_index(nums):
    if not nums:
        return None

    start = 0
    end = len(nums) - 1
    while start < end:
        mid = (start + end) >> 1
        if nums[mid] > mid:
            end = mid - 1
        elif nums[mid] < mid:
            start = mid + 1
        else:
            return mid
    return None

if __name__ == "__main__":
    print(num_equal_index([-3, -1, 1, 3, 5]))