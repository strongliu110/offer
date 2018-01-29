"""
// 面试题32（一）：不分行从上到下打印二叉树
// 题目：从上到下打印出二叉树的每个节点，同一层的节点按从左到右的顺序打印
"""

from collections import deque

# 广度优先遍历都要用到队列，因为队列是先进先出的
def bfs(tree):
    if not tree:
        return None

    queue = deque([tree])
    ret = []
    while queue:
        node = queue.popleft()
        ret.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ret

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

if __name__ == '__main__':
    tree = Tree()
    tree.construct_tree([1, 2, 3, 4, 5, 6, 7])
    print(tree.bfs())
    print(bfs(tree.root))
