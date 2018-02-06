"""
// 面试题55（二）：平衡二叉树
// 题目：输入一棵二叉树的根结点，判断该树是不是平衡二叉树。如果某二叉树中
// 任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
"""

from collections import deque

# 采用后序遍历
def is_balance(tree):
    if not tree:
        return True, 0

    balance1, left = is_balance(tree.left)
    balance2, right = is_balance(tree.right)
    if balance1 and balance2:
        if abs(left - right) <= 1:
            return True, max(left, right) + 1
    return False, None

def is_balance2(tree):
    if not tree:
        return True

    def deep(tree):
        if not tree:
            return 0
        return max(deep(tree.left), deep(tree.right)) + 1

    left = deep(tree.left)
    right = deep(tree.right)
    if abs(left - right) > 1:
        return False

    return is_balance2(tree.left) and is_balance2(tree.right)

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
    tree.construct_tree([1, 2, None, 4])
    print(is_balance(tree.root))
    print(is_balance2(tree.root))