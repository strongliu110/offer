"""
// 面试题39：数组中出现次数超过一半的数字
// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
// 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
// 出现了5次，超过数组长度的一半，因此输出2。
"""

import random

# 快速排序，时间O(nlogn)
def quick_sort(data, left, right):
    if left > right:
        return data

    i, j = left, right
    base = data[i]

    while i < j:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while i < j and data[j] >= base:
            j = j - 1

        # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
        data[i] = data[j]

        # 同样的方式比较前半区
        while i < j and data[i] <= base:
            i = i + 1
        data[j] = data[i]
    # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
    data[i] = base

    # 递归前后半区
    quick_sort(data, left, i - 1)
    quick_sort(data, j + 1, right)

    return data


# 分割为左小右大两部分，返回中值的索引
def partition(data, left, right):
    base = data[left]
    while left < right:
        while left < right and data[right] >= base:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= base:
            left += 1
        data[right] = data[left]
    data[left] = base

    return left

# 快速排序
def quickSoft(data, left, right):
    if left < right:
        base = partition(data, left, right)
        quickSoft(data, left, base - 1)
        quickSoft(data, base + 1, right)
    return data

# 基于分割函数，时间O(n)
def more_half_num(numbers):
    middle = len(numbers) >> 1
    left = 0
    right = len(numbers) - 1
    index = partition(numbers, left, right)
    while index != middle:
        if index > middle:
            index = partition(numbers, left, index - 1)
        else:
            index = partition(numbers, index + 1, right)
    return numbers[middle]

# 统计出现的次数大于一半。时间O(n)
def more_half_num2(numbers):
    times = dict()
    for num in numbers:
        times[num] += 1 if times.get(num) else 1
        if times[num] > (len(numbers) >> 1):
            return num
    return None

if __name__ == '__main__':
    data1 = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    data2 = data1[:]  # 深复制，互不相关
    print(quick_sort(data1, 0, len(data1) - 1))
    print(quickSoft(data2, 0, len(data2) - 1))

    test = [1, 2, 1, 2, 3, 1, 1]
    test2 = test[:]
    print(more_half_num(test))
    print(more_half_num(test2))