"""
// 面试题50（一）：字符串中第一个只出现一次的字符
// 题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
// 'b'。
"""

# 使用两个hash，一个记录每个字符出现的次数，另一个记录每个字符第一次出现的位置
def first_not_repeating_char(str):
    if not str:
        return None

    count = {}
    location = {}
    for k, s in enumerate(str):
        count[s] = count[s] + 1 if count.get(s) else 1
        if s not in location:
            location[s] = k
    ret = float('inf')  # 最大的整数
    for k in location.keys():
        if count.get(k) == 1 and location[k] < ret:
            return location[k], k
    return ret

if __name__ == '__main__':
    test = 'abaccbdse'
    print(first_not_repeating_char(test))