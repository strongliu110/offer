"""
// 面试题36：二叉搜索树与双向链表
// 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
// 不能创建任何新的结点，只能调整树中结点指针的指向。
"""

from collections import deque

# 中序遍历，根结点的left指向左子树的最后一个(最大)值，right指向右子树的(最小)值
def convert(tree):
    if not tree:
        return None
    p_last = convert_nodes(tree, None)  # 结点转换
    while p_last and p_last.left:  # 获取链表头结点
        p_last = p_last.left
    return p_last

def convert_nodes(tree, last):
    if not tree:
        return None
    if tree.left:
        last = convert_nodes(tree.left, last)
    if last:
        last.right = tree
    tree.left = last
    last = tree
    if tree.right:
        last = convert_nodes(tree.right, last)
    return last

def print_nodes(tree):
    # 正序链表打印
    ret = []
    while tree:
        tmp = []
        tmp.append(tree.left.val if tree.left else None)
        tmp.append(tree.val)
        tmp.append(tree.right.val if tree.right else None)
        ret.append(tmp)
        tree = tree.right
    print(ret)

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def construct_tree(self, values):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])

        length = len(values)
        num = 1
        while num < length:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[num]) if values[num] else None
                queue.append(node.left)
                if num + 1 < length:
                    node.right = TreeNode(values[num + 1]) if values[num + 1] else None
                    queue.append(node.right)
                    num += 1
                num += 1

if __name__ == '__main__':
    r = Tree()
    r.construct_tree([5, 3, 6, 2, 4, None, 7, 1])
    t = convert(r.root)
    print_nodes(t)