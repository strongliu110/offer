"""
// 面试题54：二叉搜索树的第k个结点
// 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。
"""

from collections import deque

# 二叉树中序遍历是递增排序的
def kth_node(tree, k):
    if not tree:
        return None

    ret = []
    def in_order(tree):
        if not tree:
            return
        in_order(tree.left)
        ret.append(tree.data)
        in_order(tree.right)

    in_order(tree)

    return ret[k - 1]

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def bfs(self):
        """广度优先遍历(采用队列实现)"""
        ret = []
        queue = deque([self.root])  # 注意中括号
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        return ret

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

if __name__ == "__main__":
    tree = Tree()
    tree.construct_tree([5, 3, 7, 2, 4, 6, 8])
    print(kth_node(tree.root, 3))