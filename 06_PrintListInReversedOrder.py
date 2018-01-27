"""
// 面试题6：从尾到头打印链表
// 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""

class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Link(object):

    @staticmethod
    def link(array):
        if len(array) <= 0:
            return None

        head = ListNode(0)  # 引入head简化
        move = head
        for num in array:
            node = ListNode(num)
            move.next = node
            move = move.next
        return head.next

# 基于栈实现反转
def reverse(links):
    stack = []
    while links:
        stack.append(links)
        links = links.next

    while stack:
        link = stack.pop()
        print(link.data)

# 基于递归实现反转。递归本质就是栈结构，层次很深时存在栈溢出问题
def reverse1(links):
    if links:
        reverse1(links.next)
        print(links.data)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    links = Link.link(array)

    reverse(links)
    reverse1(links)
