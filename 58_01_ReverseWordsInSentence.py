"""
// 面试题58（一）：翻转单词顺序
// 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
// 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
// 则输出"student. a am I"。
"""

def reverse_words(sentence):
    if not sentence:
        return None

    tmp = sentence.split()
    return "".join(tmp[::-1])  # 使用join效率更好，+每次都会创建新的字符串

if __name__ == '__main__':
    test = 'I am a engineer.'
    print(reverse_words(test))