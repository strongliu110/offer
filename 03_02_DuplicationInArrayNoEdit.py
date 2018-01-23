# coding=utf-8

"""
// 面试题3（二）：不修改数组找出重复的数字
// 题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
// 少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
// 数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
// 输出是重复的数字2或者3。
"""

# 二分查找，时间O(nlogn),空间O(1)
def duplicate(arr):
    start = 1
    end = len(arr) - 1  # 获取长度
    while end >= start:
        middle = ((end - start) >> 1) + start  # 若用/2，需要转成int。也可直接用//2，另外注意>>优先级
        count = countRange(arr, start, middle)
        if end == start:
            if count > 1:
                return start
            else:
                break

        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return -1

def countRange(arr, start, end):
    count = 0
    for index, num in enumerate(arr):
        if (num >= start) and (num <= end):
            count += 1  # 没有++
    return count

if __name__ == "__main__":
    arr = [2, 3, 5, 4, 3, 2, 6, 7]
    print(duplicate(arr))