"""
// 面试题32（二）：分行从上到下打印二叉树
// 题目：从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层
// 打印到一行。
"""

from collections import deque

def bfs(tree):
    if not tree:
        return None

    queue = deque([tree])
    next_level = 0  # 下一层节点数
    to_be_printed = 1  # 当前层未打印的节点数
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        to_be_printed -= 1
        if node.left:
            queue.append(node.left)
            next_level += 1
        if node.right:
            queue.append(node.right)
            next_level += 1
        if to_be_printed == 0:
            print("")
            to_be_printed = next_level
            next_level = 0

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
    tree.construct_tree([8, 6, 10, 5, 7, 9, 11])
    bfs(tree.root)