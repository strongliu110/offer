"""
// 面试题23：链表中环的入口结点
// 题目：一个链表中包含环，如何找出环的入口结点？例如，在图3.8的链表中，
// 环的入口结点是结点3。
"""

# 1、先使用快慢指针相遇判断是否有环
# 2、如果有环，则从相遇位置（必在环中）计数，若再回到这个位置就是环中节点数
# 3、得到节点数n后采用双指针，一个先走n步，相遇处即为入口

def meeting_node(link):
    if not link:
        return None

    slow = link.next
    fast = slow.next
    while fast and slow:
        if fast == slow:
            return fast
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

def entry_node(link):
    node = meeting_node(link)
    if not node:
        return None

    # 得到环中节点数
    nodesInLoop = 1
    move = node
    while move.next != node:
        move = move.next
        nodesInLoop += 1

    fast = link
    for i in range(nodesInLoop):
        fast = fast.next

    slow = link
    while slow != fast:
        fast = fast.next
        slow = slow.next
    return slow.val


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

        move.next = head.next.next
        return head.next

if __name__ == "__main__":
    link = Link.link((1, 2, 3, 4, 5, 6))
    print(entry_node(link))