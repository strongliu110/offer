"""
// 面试题52：两个链表的第一个公共结点
// 题目：输入两个链表，找出它们的第一个公共结点。
"""

# 可以使用两个辅助栈

# 先获取到两个链表的长度，然后长的链表先走多的几步，之后一起遍历
def first_common_node(link1, link2):
    if not link1 or not link2:
        return None

    length1 = length2 = 0
    move1, move2 = link1, link2
    while move1:  # 获取链表长度
        length1 += 1
        move1 = move1.next
    while move2:
        length2 += 1
        move2 = move2.next

    while length1 > length2:  # 长链表先走多的长度
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next

    while link1:  # 链表一起走
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None