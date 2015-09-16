class GenerateParenthesis:

    def __init__(self, n):
        self.n = n
        self.token1 = ['(' for i in range(n)]
        self.token2 = [')' for i in range(n)]
        self.my_stack = []
        self.results = set()




    def back_track(self, cur, A):

        if cur == 2 * self.n:
            self.results.add(''.join(A))
            return

        if len(self.token1) != 0:
            char = self.token1.pop()
            A.append(char)
            self.my_stack.append(char)
            self.back_track(cur + 1, A)

            self.my_stack.pop()
            del A[-1]
            self.token1.append(char)

        if len(self.my_stack) != 0:
            tmp = self.my_stack.pop()
            char = self.token2.pop()
            A.append(char)
            self.back_track(cur + 1, A)
            self.my_stack.append(tmp)
            self.token2.append(char)
            del A[-1]



class Solution:
    def generateParenthesis(self, n):
        g = GenerateParenthesis(n)
        g.back_track(0,[])
        print(g.results)
        return g.results



if __name__ == '__main__':
    Solution().generateParenthesis(1)

