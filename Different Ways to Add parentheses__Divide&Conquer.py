__author__ = 'WangZhe'
import re
op_dict = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y
}


def divide_and_conquer(num, opr):
        length = len(opr)   # num_length = length + 1
        if length == 0:
            return [num[0]]
        if length == 1:
            return [op_dict[opr[0]](num[0], num[1])]
        else:
            result = []
            for k in range(length):
                left_num = num[0: k + 1]
                right_num = num[k + 1: length + 1]
                left_opr = opr[0: k]
                right_opr = opr[k + 1: length]
                left_result = divide_and_conquer(left_num, left_opr)
                right_result = divide_and_conquer(right_num, right_opr)
                for i in left_result:
                    for j in right_result:
                        result += [op_dict[opr[k]](i, j)]
            return result


class Solution:
    # @param {string} input
    # @return {integer[]}

    def diffWaysToCompute(self, input):
        num = re.split('\+|-|\*', input)
        opr = re.split('\d+', input)
        opr = opr[1: -1]
        num = [int(i) for i in num]
        return divide_and_conquer(num, opr)
