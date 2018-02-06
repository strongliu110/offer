"""
// 面试题55（一）：二叉树的深度
// 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
// 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

from collections import deque

# 采用递归。分别求左右子树深度后+1
def deep(tree):
    if not tree:
        return 0
    left = deep(tree.left)
    right = deep(tree.right)
    return max(left, right) + 1

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
    tree.construct_tree([1, 2, 3, 4])
    print(deep(tree.root))