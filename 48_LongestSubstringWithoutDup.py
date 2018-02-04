"""
// 面试题48：最长不含重复字符的子字符串
// 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
// 字符串的长度。假设字符串中只包含从'a'到'z'的字符。
"""

# 动态规划,f(i)=f(i-1)+1
def max_length_substring(s):
    res = 0
    if not s:
        return res

    d = {}
    start = 0
    for i in range(len(s)):
        if s[i] in d and d[s[i]] >= start:
            start = d[s[i]] + 1
        tmp = i - start + 1
        d[s[i]] = i
        res = max(res, tmp)
    return res

if __name__ == "__main__":
    str = "abcacfrar"
    print(max_length_substring(str))