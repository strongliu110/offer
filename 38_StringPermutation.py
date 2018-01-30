"""
// 面试题38：字符串的排列
// 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
// 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。
"""

from itertools import permutations

def my_permutation(str):
    ret = []
    str_set = []

    def permutation(str):
        for i in str:
            str_tem = str.replace(i, "")
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append("".join(str_set))
            str_set.pop()

    permutation(str)
    return ret

if __name__ == '__main__':
    s = 'abc'
    print(my_permutation(s))
    print([''.join(p) for p in permutations(s)])
