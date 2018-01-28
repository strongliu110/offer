"""
// 面试题28：对称的二叉树
// 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
// 它的镜像一样，那么它是对称的。
"""

from collections import deque

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

def symmetrical(tree):
    return _symmetrical(tree, tree)

def _symmetrical(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif not tree1 or not tree2:
        return False
    elif tree1.val != tree2.val:
        return False

    return _symmetrical(tree1.left, tree2.right) and _symmetrical(tree1.right, tree2.left)

if __name__ == '__main__':
    tree = Tree()
    tree.construct_tree([8, 6, 6, 5, 7, 7, 5])
    print(symmetrical(tree.root))

    tree2 = Tree()
    tree2.construct_tree([8, 7, 7, 6, 6, 6])
    print(symmetrical(tree2.root))