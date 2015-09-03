__author__ = 'WangZhe'


class Calculator:

    def __init__(self):
        self.operator = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

        self.opr_dict = {
            '+': lambda x, y: float(x) + float(y),
            '-': lambda x, y: float(x) - float(y),
            '*': lambda x, y: float(x) * float(y),
            '/': lambda x, y: float(x) / float(y)
        }

    def is_token(self, x):
        return x == '(' or x == ')' or x in self.operator

    def parse_2_infix(self, expression):
        i = 0
        infix = []
        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif self.is_token(expression[i]):
                infix.append(expression[i])
                i += 1
            else:
                tmp = i
                while i < len(expression) and not self.is_token(expression[i]):
                    i += 1
                infix.append(expression[tmp: i])
        return infix



    def infix_2_postfix(self, infix):
        postfix = []
        s = []

        it = 0
        while it < len(infix):
            i = infix[it]
            if i == '(':
                s.append(i)
                it += 1
            elif i == ')':
                while len(s) > 0 and s[-1] != '(':
                        token = s.pop()
                        postfix.append(token)
                s.pop()
                it += 1
            elif i not in self.operator:
                postfix.append(i)
                it += 1
            else:
                if len(s) == 0:
                    s.append(i)
                    it += 1
                elif self.precedence[i] > self.precedence[s[-1]]:
                    s.append(i)
                    it += 1
                elif self.precedence[i] <= self.precedence[s[-1]]:
                    while len(s) > 0 and self.precedence[s[-1]] >= self.precedence[i]:
                        token = s.pop()
                        postfix.append(token)
                    s.append(i)
                    it += 1
        while len(s) > 0:
            postfix.append(s.pop())
        return postfix

    def eval_postfix(self, postfix):
        s = []
        for i in postfix:
            if i in self.operator:
                tmp2 = s.pop()
                tmp1 = s.pop()
                result = self.opr_dict[i](tmp1, tmp2)
                s.append(result)
            else:
                s.append(i)
        return s[0]


class Solution:

    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        c = Calculator()
        return int(c.eval_postfix(c.infix_2_postfix(c.parse_2_infix(s))))


