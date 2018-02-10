"""
// 面试题66：构建乘积数组
// 题目：给定一个数组A[0, 1, …, n-1]，请构建一个数组B[0, 1, …, n-1]，其
// 中B中的元素B[i] =A[0]×A[1]×… ×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
"""

def multiply(nums1):
    if not nums1:
        return nums1

    nums2 = {}
    nums2[0] = 1
    for i in range(1, len(nums1)):
        nums2[i] = nums2[i - 1] * nums1[i - 1]

    tmp = 0
    for i in range(0, len(nums1)-2, -1):
        tmp *= nums1[i + 1]
        nums2[i] *= tmp
    return nums2.values()

if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]
    print(multiply(test))