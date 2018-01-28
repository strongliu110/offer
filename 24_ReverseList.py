"""
// 面试题24：反转链表
// 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
// 头结点。
"""

# 需要在调整节点的next之前，保存下一个节点，以防链表断开
def reverse_list(link):
    node = link
    prev_node = None
    reverse = None
    while node:
        next_node = node.next  # 缓存下一个节点
        if not next_node:
            reverse = node

        node.next = prev_node
        prev_node = node
        node = next_node
    return reverse


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
    link = Link.link([1, 2, 3, 4, 5])
    Link.print_link(link)
    reverse = reverse_list(link)
    Link.print_link(reverse)