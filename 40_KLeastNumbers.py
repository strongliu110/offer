"""
// 面试题40：最小的k个数
// 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
// 这8个数字，则最小的4个数字是1、2、3、4。
"""

import random
import heapq

# 采用快速排序，时间O(nlogn)

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


# 快排分割时，如果基于数组的第k个数字来调整，则比它小的数字都在左边，比它大的都在右边。时间O(n)
def least_numbers(nums, k):
    if len(nums) <= k:
        return nums

    left = 0
    right = len(nums) - 1
    index = partition(nums, left, right)
    while index != k - 1:
        if index > k - 1:
            index = partition(nums, left, index - 1)
        else:
            index = partition(nums, index + 1, right)

    return nums[0: k]

# 使用heapq，该模块是一个最小堆，需要转化成最大堆，只要在入堆的时候把值取反就可以转化成最大堆，仅适用于数字。时间O(nlogk)
class MaxHeap(object):
    def __init__(self, k):
        self.k = k
        self.heap = []

    def push(self, item):
        item = -item
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        else:
            least = self.heap[0]  # 查看堆顶元素
            if item > least:
                heapq.heapreplace(self.heap, item)  # 弹出一个最小值，然后将item插入到堆当中

    def least_numbers(self):
        return [-x for x in self.heap]

if __name__ == '__main__':
    test = [4, 5, 1, 6, 2, 7, 3, 8]
    print(least_numbers(test, 4))

    test1 = random.sample(range(100000), 100)
    test2 = test1[:]
    print(least_numbers(test1, 4))
    h = MaxHeap(4)
    for t in test2:
        h.push(t)
    print(h.least_numbers())
