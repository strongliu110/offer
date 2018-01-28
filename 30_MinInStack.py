"""
// 面试题30：包含min函数的栈
// 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
// 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。
"""

# 使用一个辅助栈保存最小值。使用变量保存会出现最小值被弹出后无法得到下一个最小值
class Stack(object):
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)

        if not self.min or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        if not self.stack:
            return None

        self.min.pop()
        return self.stack.pop()

    def min(self):
        if not self.min:
            return None

        return self.min[-1]

if __name__ == '__main__':
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(2)
    print(s.stack)
    print(s.min)