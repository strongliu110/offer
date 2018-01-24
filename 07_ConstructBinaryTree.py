"""
// 面试题7：重建二叉树
// 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
// 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
// 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
// 图2.6所示的二叉树并输出它的头结点。
"""

from collections import deque

"""
bfs用队列实现，dfs用栈实现
"""

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        """前向遍历"""
        ret = []

        def order(head):
            if not head:
                return
            ret.append(head.data)
            order(head.left)
            order(head.right)

        order(self.root)
        return ret

    def in_order(self):
        """中序遍历"""
        ret = []

        def order(head):
            if not head:
                return
            order(head.left)
            ret.append(head.data)
            order(head.right)

        order(self.root)
        return ret

    def post_order(self):
        """后序遍历"""
        ret = []

        def order(head):
            if not head:
                return
            order(head.left)
            order(head.right)
            ret.append(head.data)

        order(self.root)
        return ret

    def bfs(self):
        """广度优先遍历(采用队列实现)"""
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.data)
                queue.append(node.left)
                queue.append(node.right)

        return ret

def construct_tree(preOrder, inOrder):
    """
    前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
    :return:
    """

    if not preOrder or not inOrder:
        return None

    index = inOrder.index(preOrder[0])
    left = inOrder[:index]
    right = inOrder[index+1:]

    root = TreeNode(preOrder[0])
    root.left = construct_tree(preOrder[1: 1+len(left)], left)
    root.right = construct_tree(preOrder[-len(right):], right)
    return root


if __name__ == "__main__":
    root = construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    tree = Tree(root)
    print(tree.pre_order())
    print(tree.in_order())
    print(tree.post_order())
    print(tree.bfs())
