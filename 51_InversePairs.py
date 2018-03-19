"""
// 面试题51：数组中的逆序对
// 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
// 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
"""

import copy


# 归并排序（分治）。时间O(nlogn)，空间O(n)
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    num = len(nums) // 2
    left = merge_sort(nums[:num])  # 左边有序
    right = merge_sort(nums[num:])  # 右边有序
    return merge(left, right)  # 再将二个有序数列合并


def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


# 先把数组依次拆开，然后合并的时候统计逆序对数目，并排序
def inverse_pairs(nums):
    if not nums:
        return 0

    start, end = 0, len(nums) - 1
    tmp = copy.deepcopy(nums)
    return inverse_pairs_core(tmp, start, end)

def inverse_pairs_core(nums, start, end):
    if start == end:  # 递归结束条件
        return 0

    length = (end - start) // 2
    left = inverse_pairs_core(nums, start, start + length)
    right = inverse_pairs_core(nums, start + length + 1, end)

    # i 初始化为前半段最后一个数字的下标
    i = start + length
    # j 初始化为后半段最后一个数字的下标
    j = end
    # 本次逆序对数目
    count = 0
    t = []
    while i >= start and j >= start + length + 1:
        if nums[i] > nums[j]:
            t.append(nums[i])
            count += j - start - length
            i -= 1
        else:
            t.append(nums[j])
            j -= 1
    while i >= start:
        t.append(nums[i])
        i -= 1
    while j >= start + length + 1:
        t.append(nums[j])
        j -= 1
    nums[start:end + 1] = t[::-1]  # 倒序
    return count + left + right

if __name__ == '__main__':
    test = [7, 5, 6, 4, 8, 1, 2, 9]
    print(inverse_pairs(test))

    test2 = [1, 2, 3, 4, 5, 6, 7, 90, 21, 23, 45]
    print(merge_sort(test2))
