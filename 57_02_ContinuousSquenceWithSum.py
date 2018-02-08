"""
// 面试题57（二）：为s的连续正数序列
// 题目：输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）。
// 例如输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以结果打印出3个连续序列1～5、
// 4～6和7～8。
"""

def continuous_squence(sum):
    if sum < 3:
        return

    small = 1
    big = 2
    middle = (1 + sum) / 2  # 至少有两个数
    current = small + big

    ret = []
    while small < middle:
        if current == sum:
            ret.append([small, big])

        while current > sum and small < middle:
            current -= small
            small += 1
            if current == sum:
                ret.append([small, big])

        big += 1
        current += big

    return ret

if __name__ == "__main__":
    print(continuous_squence(15))