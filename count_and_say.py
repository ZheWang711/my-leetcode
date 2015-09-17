__author__ = 'zhewang711'
class Solution(object):

    def _read_digit(self, char, times):
        return str(times)+char

    def _next(self, string):
        result = []
        i = 0
        current_char = string[0]
        current_times = 0
        while i < len(string):
            while i < len(string) and current_char == string[i]:
                current_times += 1
                i = i + 1
            result.append(self._read_digit(current_char, current_times))
            if i != len(string):
                current_char = string[i]
                current_times = 0
        return ''.join(result)



    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        tmp = '1'
        for i in range(n - 1):
            tmp = self._next(tmp)
        return tmp

if __name__ == '__main__':
    print(Solution().countAndSay(7))