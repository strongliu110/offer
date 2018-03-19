"""
// 面试题34：二叉树中和为某一值的路径
// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
"""

from collections import deque

# 用前序遍历访问节点时，把节点添加到路径上，并累加节点值。直到为叶节点，且路径中节点值的和相等
def find_path(tree, num):
    if not tree:
        return False

    ret = []

    path = [tree]
    sums = [tree.val]
    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1] + tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        # 是叶节点，且路径和相等
        if not tree.left and not tree.right:
            if sums[-1] == num:
                ret.append([node.val for node in path])  # 注意下这里for的使用方式
        path.pop()
        sums.pop()

    dfs(tree)
    return ret


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
    t = Tree()
    t.construct_tree([10, 5, 12, 4, 7])
    print(find_path(t.root, 22))