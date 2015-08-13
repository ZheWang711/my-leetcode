__author__ = 'WangZhe'
import re

opr_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}


def delete_extra_spaces(s):
    r = []
    for i in s:
        if i != ' ':
            r.append(i)
    return ''.join(r)


def leaf_expr(s):
    num = re.split('\+|-', s)
    opr = re.split('\d+', s)
    opr = opr[1: -1]
    num = [int(i) for i in num]
    if len(opr) != len(num) - 1:
        raise ValueError('NOT LEAF EXPRESSION {0}'.format(s))
    result = num[0]
    for i in range(len(opr)):
        result = opr_dict[opr[i]](result, num[i + 1])
    return result


def cal_max_level(s):
    max = 0
    level = 0
    for i in s:
        if i == '(':
            level += 1
        if i == ')':
            max = level if level > max else max
            level -= 1
    return max


def calculator(s):
    level_s = cal_max_level(s)
    if level_s == 0:
        return leaf_expr(s)
    base_opr = []
    base_left_pth = []
    base_right_pth = []
    level = 0

    values = []
    i = 0
    while i < len(s):
        if s[i].isdigit() and level == 0:
            low = i
            while i < len(s) and s[i].isdigit():
                i += 1
            i -= 1
            high = i
            values.append(int(s[low: high + 1]))
        if s[i] == '(':
            level += 1
            if level == 1:
                base_left_pth.append(i)
                values.append(None)
        elif s[i] == ')':
            if level == 1:
                base_right_pth.append(i)
            level -= 1
        elif not s[i].isdigit() and level == 0:
            base_opr.append(i)
        i += 1

    if len(base_opr) == 0:
        return calculator(s[1: -1])
    else:
        term = 0
        for i in range(len(values)):
            if values[i] is None:
                values[i] = calculator(s[base_left_pth[term]+1: base_right_pth[term]])
                term += 1

        result = values[0]
        for i in range(len(base_opr)):
            result = opr_dict[s[base_opr[i]]](result, values[i + 1])
        return result


class Solution:
    # @param {string} s
    # @return {integer}


    def calculate(self, s):
        s = delete_extra_spaces(s)
        return calculator(s)

print(Solution().calculate('(1+(4+5+2)-3)+(6+8)'))
