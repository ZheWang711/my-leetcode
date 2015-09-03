__author__ = 'WangZhe'
import re
import timeit


class GlobalTimer:

    def __init__(self, val):
        self.value = val

    def add(self, val):
        self.value += val

    def __str__(self):
        return str(self.value)

leaf_timer = GlobalTimer(0)
total_timer = GlobalTimer(0)
cal_max_level_timer = GlobalTimer(0)
loop_timer = GlobalTimer(0)


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

    start_cal_max_level = timeit.default_timer()
    level_s = cal_max_level(s)        # calculate the max level of expression s
    cal_max_level_timer.add(timeit.default_timer() - start_cal_max_level)

    if level_s == 0:    # recursion terminates
        start_time = timeit.default_timer()
        result = leaf_expr(s)
        leaf_timer.add(timeit.default_timer() - start_time)
        return result

    # initialize some variables for the following while loop
    base_opr = []           # the index list of base operator, whose level is 0
    base_left_pth = []      # the index list of base '(', whose level is 1
    base_right_pth = []     # the index list of base ')', whose level is 1
    level = 0               # level count, start with 0
    # a value list containing 0-level numbers, and place holders (None) for each sub-expressions
    values = []   # initialize with empty list

    start_loop = timeit.default_timer()
    # the following while loop constructs the above lists ( base_opr, base_left_pth, base_right_pth, values )
    i = 0   # a pointer to each chars
    while i < len(s):
        if s[i].isdigit() and level == 0:   # level-0 number, append its value to 'values'
            low = i
            while i < len(s) and s[i].isdigit():
                i += 1
            i -= 1
            high = i
            values.append(int(s[low: high + 1]))
        elif s[i] == '(':   # sub-expression, append a None to 'values', record its index in base_left_pth
            level += 1
            if level == 1:
                base_left_pth.append(i)
                values.append(None)
        elif s[i] == ')':   # sub-expression closing parenthesis, i.e. ), record its index in base_right_pth
            if level == 1:
                base_right_pth.append(i)
            level -= 1
        elif not s[i].isdigit() and level == 0:     # 0-level operators, records its index in base_opr
            base_opr.append(i)
        i += 1
    loop_timer.add(timeit.default_timer() - start_loop)

    # for the case of a pair of parenthesis containing all the expression, e.g. (a + b + c)
    if len(base_opr) == 0:
        return calculator(s[1: -1])
    # otherwise, there must be at least one 0-level operator and two sub-expressions
    else:
        # divide
        term = 0
        for i in range(len(values)):
            if values[i] is None:
                values[i] = calculator(s[base_left_pth[term]+1: base_right_pth[term]])
                term += 1
        # conquer
        result = values[0]
        for i in range(len(base_opr)):
            result = opr_dict[s[base_opr[i]]](result, values[i + 1])
        return result


class Solution:
    # @param {string} s
    # @return {integer}


    def calculate(self, s):
        start = timeit.default_timer()
        s = delete_extra_spaces(s)
        result = calculator(s)
        total_timer.add(timeit.default_timer() - start)
        print('total time', total_timer)
        print('leaf expression', leaf_timer)
        print('calculate max level', cal_max_level_timer)
        print('loop time', loop_timer)
        return result

