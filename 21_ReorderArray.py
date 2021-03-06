"""
// 面试题21：调整数组顺序使奇数位于偶数前面
// 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
// 奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

def reorder(arr, func):
    # 使用两个指针，前后各一个，为了更好的扩展性，可以把判断奇偶部分抽取出来
    left = 0
    right = len(arr) - 1
    while left < right:
        while left < right and not func(arr[left]):
            left += 1
        while left < right and func(arr[right]):
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

def is_even(num):
    return (num & 1) == 0

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    reorder(arr, is_even)
    print(arr)