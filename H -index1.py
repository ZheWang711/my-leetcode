__author__ = 'zhewang711'


class Solution(object):
    def hIndex(self, citations):
        tmp = sorted(citations)
        for i in range(len(tmp) - 1, -1, -1):
            # 1. sort array A ==> for all i : A[i] <= a[i + 1]
            # 2.scan A from right to left to find the largest i such that
            #   y = len(A) - i is the # of elements whose value is larger than or equal to A[i].
            #   Since a[index] >= y,
            #   there are y elements in array A whose value is larger than a[index] and larger than y,
            #   which means that y is a possible H-index.
            # In the y + 1 most largest elements (from a[i-1] to a[-1]),
            # because a[i-1] < y + 1, there are only y elements whose
            # value might >= y + 1, so y + 1 is not a possible H-index.
            # Since y is a possible H-index and y + 1 is not a possible H-index, y is the final H-index.
            y = len(tmp) - i
            if i == 0 and y <= tmp[i] or y <= tmp[i] and y + 1 > tmp[i - 1]:
                return y
        return 0    # H-index is 0 iff all citation elements is 0.

