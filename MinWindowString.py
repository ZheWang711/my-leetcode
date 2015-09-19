__author__ = 'zhewang711'
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needs = collections.Counter(t)
        current_window = {i: 0 for i in needs.keys()}
        missing = len(t)
        J = I = None
        i = j = 0
        while j < len(s):
            if s[j] not in needs:
                j += 1
                continue
            current_window[s[j]] += 1
            if current_window[s[j]] <= needs[s[j]]:
                missing -= 1
            if missing == 0:
                # the following while loop can be paced outside :if: condition, place here to improve performance
                while i <= j and (needs.get(s[i]) is None or current_window[s[i]] > needs[s[i]]):
                    if needs.get(s[i]) is not None:
                        current_window[s[i]] -= 1
                    i += 1
                if J is None or j - i < J - I:
                    J, I = j, i
            j += 1
        if missing > 0:
            return ''
        else:
            return s[I: J + 1]
if __name__ == '__main__':
    print(Solution().minWindow("acbbaca", "aba"))




        