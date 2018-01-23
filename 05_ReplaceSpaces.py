"""
// 面试题5：替换空格
// 题目：请实现一个函数，把字符串中的每个空格替换成"%20"。例如输入“We are happy.”，
// 则输出“We%20are%20happy.”。
"""

def replace(str):
    return str.replace(" ", "%20")

def replace1(str):
    b = ""
    for i in str:
        if i == " ":
            b += "%20"
        else:
            b += i
    return b

print(replace("hello world"))
print(replace1("hello world"))