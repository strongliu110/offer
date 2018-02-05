"""
// 面试题53（一）：数字在排序数组中出现的次数
// 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
// 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。
"""

# 使用二分法分别找到数组中第一个和最后一个出现的值的坐标，然后相减

def first_k(nums, k):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < k:  # 后半段
            if mid + 1 < len(nums) and nums[mid + 1] == k:  # 后半段第一个数等于k
                return mid + 1
            left = mid + 1
        elif nums[mid] > k:  # 前半段
            if mid - 1 < 0 or (mid - 1 >= 0 and nums[mid - 1] < k):  # 前半段只有一个数，或前半段最后一个数小于k
                return mid
            right = mid - 1
        else:
            right = mid - 1
    return -1

def last_k(nums, k):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < k:  # 后半段
            left = mid + 1
        elif nums[mid] > k:  # 前半段
            if mid - 1 >= 0 and nums[mid - 1] == k:  # 前半段的最后一个数等于k
                return mid - 1
            right = mid - 1
        else:
            if mid + 1 == len(nums) or (mid + 1 < len(nums) and nums[mid + 1] > k):  # 后半段只有一个数，或后半段下一个数大于k
                return mid
            left = mid + 1
    return -1

def k_counts(nums, k):
    first = first_k(nums, k)
    last = last_k(nums, k)
    if first < 0 and last < 0:
        return 0
    elif first < 0 or last < 0:
        return 1
    else:
        return last - first + 1

if __name__ == '__main__':
    test = [1, 2, 3, 3, 3, 3, 4, 5]
    print(k_counts(test, 3))