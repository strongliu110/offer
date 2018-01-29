"""
// 面试题32（三）：之字形打印二叉树
// 题目：请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺
// 序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，
// 其他行以此类推。
"""

from collections import deque

# 需要两个栈来实现
def print_in_zigzag(tree):
    if not tree:
        return None

    queue0 = [tree]
    queue1 = []

    current = 0
    while queue0 or queue1:
        if current == 0:
            node = queue0.pop()  # 弹出末尾元素
        else:
            node = queue1.pop()
        print(node.val, end=" ")

        if current == 0:
            if node.left:
                queue1.append(node.left)
            if node.right:
                queue1.append(node.right)
        else:
            if node.right:
                queue0.append(node.right)
            if node.left:
                queue0.append(node.left)

        if (current == 0 and not queue0) or (current == 1 and not queue1):
            current = 1 - current

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
    tree = Tree()
    tree.construct_tree([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print_in_zigzag(tree.root)