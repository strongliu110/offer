"""
// 面试题26：树的子结构
// 题目：输入两棵二叉树A和B，判断B是不是A的子结构。
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

def sub_tree(tree1, tree2):
    if not tree1 and tree2:
        return False

    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)

    return True

if __name__ == "__main__":
    tree1 = Tree()
    tree1.construct_tree([1, 2, 3, 4, 5])
    print(tree1.bfs())
    tree2 = Tree()
    tree2.construct_tree([2, 4, 5])
    print(tree2.bfs())
    print(sub_tree(tree1.root, tree2.root))  # 需要传root节点
