"""
// 面试题31：栈的压入、弹出序列
// 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
// 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
// 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
// 4、3、5、1、2就不可能是该压栈序列的弹出序列。
"""

# 使用一个辅助栈, 如果辅助栈栈顶元素不等于出栈元素，则从入栈中找改值，直到入栈为空
# 如果最后出栈序列为空，则是入栈的弹出序列
def pop_order(push_stack, pop_stack):
    if not push_stack or not pop_stack:
        return False

    stack = []
    while pop_stack:
        pop_val = pop_stack[0]
        if stack and stack[-1] == pop_val:  # 如果下一个弹出的元素刚好是栈顶元素，则直接弹出
            stack.pop()
            pop_stack.pop(0)
        else:
            while push_stack:  # 如果下一个弹出元素不在栈顶，则把压栈序列中未入栈数字压入辅助栈直到栈顶为止
                if push_stack[0] != pop_val:
                    stack.append(push_stack.pop(0))
                else:
                    push_stack.pop(0)
                    pop_stack.pop(0)
                    break
        if not push_stack:  # 如果所有数字都入栈后仍然未找到下一个弹出数字
            while stack:
                if stack.pop() != pop_stack.pop(0):
                    return False

    if not pop_stack:
        return True

    return False

if __name__ == "__main__":
    print(pop_order([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(pop_order([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
