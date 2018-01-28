"""
// 面试题25：合并两个排序的链表
// 题目：输入两个递增排序的链表，合并这两个链表并使新链表中的结点仍然是按
// 照递增排序的。例如输入图3.11中的链表1和链表2，则合并之后的升序链表如链
// 表3所示。
"""

# 归并排序，时间O(nlogn),空间O(n)。其中二路归并为O(n)。
def merge(link1, link2):
    if not link1:
        return link2
    elif not link2:
        return link1

    ret = None
    if link1.val < link2.val:
        ret = link1
        ret.next = merge(link1.next, link2)
    else:
        ret = link2
        ret.next = merge(link1, link2.next)
    return ret

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

    @staticmethod
    def print_link(link):
        node = link
        while node:
            print(node.val)
            node = node.next

if __name__ == "__main__":
    link1 = Link.link([1, 3, 8, 10])
    link2 = Link.link([2, 4, 9, 11])
    merge = merge(link1, link2)
    Link.print_link(merge)