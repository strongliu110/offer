"""
// 面试题37：序列化二叉树
// 题目：请实现两个函数，分别用来序列化和反序列化二叉树。
"""

def serialize(tree, ret):
    if not tree:
        ret.append("$")

    ret.append(tree.val)
    serialize(tree.left)
    serialize(tree.right)
