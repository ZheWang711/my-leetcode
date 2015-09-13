__author__ = 'zhewang711'


class ScrambleString:

    def __init__(self, string, target):
        self.target = list(target)
        self.string = list(string)

    def _divide_and_conquer(self, str_left, str_right, tar_left, tar_right):

        if str_left == str_right:
            if self.string[str_left] == self.target[tar_left]:
                return True
            else:
                return False

        alphabet_target = {}
        alphabet_string_reversed = {}
        alphabet_string = {}

        for sep in range(tar_left, tar_right):

            if alphabet_target.get(self.target[sep]) is None:
                alphabet_target[self.target[sep]] = 1
            else:
                alphabet_target[self.target[sep]] += 1

            str_sep_reversed = str_right - sep + tar_left - 1
            if alphabet_string_reversed.get(self.string[str_sep_reversed + 1]) is None:
                alphabet_string_reversed[self.string[str_sep_reversed + 1]] = 1
            else:
                alphabet_string_reversed[self.string[str_sep_reversed + 1]] += 1

            str_sep = str_left + sep - tar_left
            if alphabet_string.get(self.string[str_sep]) is None:
                alphabet_string[self.string[str_sep]] = 1
            else:
                alphabet_string[self.string[str_sep]] += 1

            if alphabet_string == alphabet_target and self._divide_and_conquer(str_left, str_sep, tar_left, sep) and self._divide_and_conquer(str_sep + 1, str_right, sep + 1, tar_right):
                return True

            if alphabet_string_reversed == alphabet_target and  self._divide_and_conquer(str_sep_reversed + 1, str_right, tar_left, sep) and self._divide_and_conquer(str_left, str_sep_reversed, sep + 1, tar_right):
                return True
        return False


class Solution(object):

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        return ScrambleString(s1, s2)._divide_and_conquer(0, len(s1) - 1, 0, len(s2) - 1)

if __name__ == '__main__':
    print(Solution().isScramble("oatzzffqpnwcxhejzjsnpmkmzngneo", "acegneonzmkmpnsjzjhxwnpqffzzto"))


