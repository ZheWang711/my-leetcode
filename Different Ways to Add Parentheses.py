__author__ = 'WangZhe'
'''
Given a string of numbers and operators, return all possible
results from computing all the different possible ways to
group numbers and operators. The valid operators are +, - and *
'''


class Node:
    def __init__(self, is_leaf=True, value=None, left=None, right=None, order_label=None, operator=None):
        self.is_leaf = is_leaf
        self.value = value
        self.left = left
        self.right = right
        self.order_label = order_label
        self.operator = operator

    def able_to_repeat(self):
        return (not self.left.is_leaf) and (not self.right.is_leaf)

    def __str__(self):
        return str(self.value)


def print_expression(root):
    if root.is_leaf:
        return str(root.value)
    else:
        string = '({0}{1}{2})'.format(print_expression(root.left), root.operator, print_expression(root.right))
        return string


def merge(t1, t2, operator, i):
    value = None
    if operator == '+':
        value = t1.value + t2.value
    if operator == '-':
        value = t1.value - t2.value
    if operator == '*':
        value = t1.value * t2.value
    return Node(False, value, t1, t2, i, operator)


# tree node list A, operator list B
def driven(A, B, result, cur, ex_set):
    if len(A) == 1:
        ex = print_expression(A[0])
        if ex not in ex_set:
            ex_set.add(ex)
            result.append(A[0].value)
    else:
        for i in range(len(B)):
            new_node = merge(A[i], A[i + 1], B[i], cur)
            if new_node.able_to_repeat() and new_node.left.order_label > new_node.right.order_label:
                continue
            # progress
            del A[i]
            del A[i]
            tmp = B[i]
            del B[i]
            A.insert(i, new_node)
            driven(A, B, result, cur + 1, ex_set)
            # recover global variables
            del A[i]
            A.insert(i, new_node.right)
            A.insert(i, new_node.left)
            B.insert(i, tmp)


class Solution:
    # @param {string} input
    # @return {integer[]}

    def diffWaysToCompute(self, input):
        A = []
        B = []
        result = []
        ex_set = set()
        i = 0
        while i < len(input):
            j = i
            while j < len(input) and input[j].isdigit():
                j += 1
            A.append(Node(value=int(input[i: j])))
            if j < len(input):
                B.append(input[j])
            i = j + 1
        driven(A, B, result, 1, ex_set)
        return result

