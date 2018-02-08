"""
// 面试题60：n个骰子的点数
// 题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s
// 的所有可能的值出现的概率。
"""

def get_probability(n):
    if n < 1:
        return None

    data1 = [0] + [1] * 6 + [0] * 6 * (n - 1)
    data2 = [0] + [0] * 6 * n
    flag = 0
    for v in range(2, n + 1):  # 控制次数
        if flag:
            for k in range(v, 6 * v + 1):
                data1[k] = sum([data2[k - j] for j in range(1, 7) if k > j])
        else:
            for k in range(v, 6 * v + 1):
                data2[k] = sum([data1[k - j] for j in range(1, 7) if k > j])
        flag = 1 - flag
    ret = []
    total = 6 ** n
    data = data2[n:] if flag else data1[n:]
    for v in data:
        ret.append(v * 1.0 / total)
    print(data)
    return ret

if __name__ == '__main__':
    print(get_probability(3))