"""
// 面试题10：斐波那契数列
// 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
"""

def fibonacci(n):
    if n < 2:
        return n

    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b

    return a


def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    num = 10
    print(fibonacci(num))
    print([n for n in fib(num)])