"""
// 面试题18（一）：在O(1)时间删除链表结点
// 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
// 结点。
"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_node(link, node):
    # 只有一个元素
    if node == link:
        del node
    # 要删除的是尾元素
    elif not node.next:
        while link:
            if link.next == node:
                link.next = None
            link = link.next
    else:
        # 把下一个元素复制到要删除的节点，然后删除下一个元素
        node.val = node.next.val
        n_node = node.next
        node.next = n_node.next
        del n_node

if __name__ == '__main__':
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    delete_node(node1, node1.next)
    print(node1.val, node1.next.val)