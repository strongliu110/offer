"""
// 面试题9：用两个栈实现队列
// 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
// 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。
"""

from collections import deque

class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()

        while self.stack1:
            value = self.stack1.pop()
            self.stack2.append(value)

        # pop 会抛异常
        return self.stack2.pop() if self.stack2 else None

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    print(q.pop())
    q.push(3)
    print(q.pop())
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())
