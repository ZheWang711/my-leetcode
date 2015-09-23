__author__ = 'zhewang711'


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        tmp = sorted(citations)
        for i in range(len(tmp) - 1, -1, -1):
            # TODO: summary
            y = len(tmp) - i
            if i == 0 and y <= tmp[i] or y <= tmp[i] and y + 1 > tmp[i - 1]:
                return y
        return 0

