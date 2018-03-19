"""
// 面试题33：二叉搜索树的后序遍历序列
// 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
// 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同。
"""

# 找根节点（后序遍历最后一个值是根结点），拆分为左右子树（比根结点小的值是左子树，剩下的是右子树），递归左右子树
def is_post_order(order):
    if not order:
        return False

    root = order[-1]
    left = 0
    while order[left] < root:
        left += 1

    right = left
    for right in range(right, len(order)):
        if order[right] < root:
            return False

    left_ret = True if left == 0 else is_post_order(order[:left])
    right_ret = True if left == right else is_post_order(order[left:right])
    return left_ret and right_ret

if __name__ == '__main__':
    print(is_post_order([5, 7, 6, 9, 11, 10, 8]))
    print(is_post_order([7, 4, 6, 5]))