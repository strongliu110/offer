"""
// 面试题22：链表中倒数第k个结点
// 题目：输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，
// 本题从1开始计数，即链表的尾结点是倒数第1个结点。例如一个链表有6个结点，
// 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个结点是
// 值为4的结点。
"""

# 用一个指针遍历不能解决问题时，可以使用两个指针。如查询链表的中间节点，可以采用一个指针走一步，另一个走两步.

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Link(object):

    @staticmethod
    def link(arr):
        if len(arr) <= 0:
            return None

        head = ListNode(0)
        move = head
        for num in arr:
            node = ListNode(num)
            move.next = node
            move = node
        return head.next

# 使用快慢指针，快的先走k-1步，需要考虑控链表以及k为0
def find_last_kth(link, k):
    # 注意鲁棒性
    if not link or k <= 0:
        return None

    move = link
    while move and k - 1 >= 0:
        move = link.next
        k -= 1

    node = link
    while move:
        move = move.next
        node = node.next

    # 防止节点数小于K
    if k != 0:
        return None
    return node.val