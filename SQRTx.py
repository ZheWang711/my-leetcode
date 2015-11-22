__author__ = 'zhewang711'
import math

class Solution(object):

    def _binary_search(self, left, right, target):
        mid = left + (right - left) // 2
        mid_sq = mid**2
        mid_p1_sq = mid_sq + 2*mid + 1
        if mid_sq == target or mid_sq < target and mid_p1_sq > target:
            return mid
        else:
            if mid_p1_sq <= target:
                return self._binary_search(mid + 1, right, target)
            else:
                return self._binary_search(left, mid - 1, target)

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = len(str(x))
        if length < 5:
            return int(math.sqrt(x))
        left = 10 ** ((length + 1)//2 -1)
        right = left * 10
        return self._binary_search(left, right, x)
