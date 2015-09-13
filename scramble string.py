__author__ = 'zhewang711'


def add_dict(dict, elem):
    '''
    Add @elem to dictionary @dict
    '''
    if dict.get(elem) is None:
        dict[elem] = 1
    else:
        dict[elem] += 1


class ScrambleString:

    def __init__(self, string, target):
        # global variables during divide and conquer
        self.target = list(target)
        self.string = list(string)

    def _divide_and_conquer(self, str_left, str_right, tar_left, tar_right):

        # basic case
        if str_left == str_right:   # the string contains only 1 element char
            if self.string[str_left] == self.target[tar_left]:
                return True
            else:
                return False

        # keeping track of number of characters that we scanned so far
        alphabet_target = {}    # in-order target
        alphabet_string_reversed = {}   # reversed order (given) string
        alphabet_string = {}    # in-order (given) string

        for sep in range(tar_left, tar_right):
            # @sep is the index of in-order target string separator
            # @str_sep_reversed is the index of reversed-order given string separator
            # @str_sep is the index of in-order given string separator

            add_dict(alphabet_target, self.target[sep])

            str_sep_reversed = str_right - sep + tar_left - 1
            add_dict(alphabet_string_reversed, self.string[str_sep_reversed + 1])

            str_sep = str_left + sep - tar_left
            add_dict(alphabet_string, self.string[str_sep])

            # string and target matches in left side
            if alphabet_string == alphabet_target and self._divide_and_conquer(str_left, str_sep, tar_left, sep) \
                    and self._divide_and_conquer(str_sep + 1, str_right, sep + 1, tar_right):
                return True
            # right string matches with left target
            if alphabet_string_reversed == alphabet_target and  self._divide_and_conquer(str_sep_reversed + 1, str_right, tar_left, sep) \
                    and self._divide_and_conquer(str_left, str_sep_reversed, sep + 1, tar_right):
                return True
        return False


class Solution(object):

    def isScramble(self, s1, s2):
        return ScrambleString(s1, s2)._divide_and_conquer(0, len(s1) - 1, 0, len(s2) - 1)

if __name__ == '__main__':
    print(Solution().isScramble("oatzzffqpnwcxhejzjsnpmkmzngneo", "acegneonzmkmpnsjzjhxwnpqffzzto"))


