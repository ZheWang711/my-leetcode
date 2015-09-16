class Solution(object):


    def _DP(self, left, right, up, down):
        if left > right or up > down:
            return
        elif left == right:
            for i in range(up, down + 1):
                self.result.append(self.matrix[i][left])
        elif up == down:
            for j in range(left, right + 1):
                self.result.append(self.matrix[down][j])
        else:
            for j in range(left, right + 1):
                self.result.append(self.matrix[up][j])
            for i in range(up + 1, down + 1):
                self.result.append(self.matrix[i][right])
            for j in range(right - 1, left - 1, -1):
                self.result.append(self.matrix[down][j])
            for i in range(down - 1, up, -1):
                self.result.append(self.matrix[i][left])
            self._DP(left + 1, right - 1, up + 1, down - 1)


    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.result = []
        self.matrix = matrix
        self._DP(0, len(matrix[0]) - 1 if len(matrix) > 0 else -1, 0, len(matrix) - 1)
        return self.result


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2], [3, 4]]))