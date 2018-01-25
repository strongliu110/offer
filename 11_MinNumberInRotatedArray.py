"""
// 面试题11：旋转数组的最小数字
// 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
// 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
// {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。
"""

# 二分法查找，时间O(logn)。适合排序数组（或部分排序）中查找值或者统计值出现的次数

def find_min(arr):
    if not arr:
        return None

    left = 0
    right = arr[-1]
    while arr[left] >= arr[right]:
        if right - left == 1:  # 退出条件
            return arr[right]

        mid = (left + right) // 2
        if arr[left] == arr[mid] == arr[right]:
            return min(arr)

        if mid >= left:
            left = mid
        if mid <= right:
            right = mid
    else:
        return arr[left]  # 当旋转后不变


if __name__ == '__main__':
    print(find_min([2, 2, 4, 5, 6, 2]))
    print(find_min([1, 0, 0, 1]))