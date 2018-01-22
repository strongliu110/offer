# coding=utf-8

"""
// 面试题3（一）：找出数组中重复的数字
// 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
// 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
// 那么对应的输出是重复的数字2或者3。
"""

# 排序后遍历，时间O(nlogn)
def duplicate1(arr):
    arr.sort()
    for index, num in enumerate(arr):  # 遍历
        if arr[index] == arr[index + 1]:
            print(num)
            return True
    return False

# 利用哈希表，时间O(n)
def duplicate2(arr):
    for num in arr:
        if arr.count(num) > 1:  # 获取数目
            print(num)
            return True
    return False

#
def duplicate3(arr):
    for index, num in enumerate(arr):
        if num != index:
            if num == arr[num]:
                print(num)
                return True
            else:
                arr[index], arr[num] = arr[num], arr[index]
    return False

if __name__ == "__main__":
    arr1 = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate1(arr1))

    arr2 = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate2(arr2))

    arr3 = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate3(arr3))

