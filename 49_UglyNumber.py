"""
// 面试题49：丑数
// 题目：我们把只包含因子2、3和5的数称作丑数（Ugly Number）。求按从小到
// 大的顺序的第1500个丑数。例如6、8都是丑数，但14不是，因为它包含因子7。
// 习惯上我们把1当做第一个丑数。
"""

def get_ugly(n):
    ugly = [1]
    t2, t3, t5 = 0, 0, 0  # 分别标记乘以2，3，5的丑数索引
    while n > 1:
        while ugly[t2] * 2 <= ugly[-1]:
            t2 += 1
        while ugly[t3] * 3 <= ugly[-1]:
            t3 += 1
        while ugly[t5] * 5 <= ugly[-1]:
            t5 += 1
        ugly.append(min([ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5]))

        n -= 1
    return ugly[-1]

if __name__ == "__main__":
    print(get_ugly(1500))