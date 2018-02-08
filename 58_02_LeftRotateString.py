"""
// 面试题58（二）：左旋转字符串
// 题目：字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
// 请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和数
// 字2，该函数将返回左旋转2位得到的结果"cdefgab"。
"""

def rotate_string(str, n):
    if not str:
        return ''

    n %= len(str)
    return str[n:] + str[:n]

if __name__ == '__main__':
    test = 'abcdefg'
    print(rotate_string(test, 2))