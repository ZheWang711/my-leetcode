__author__ = 'zhewang711'
class Solution(object):

    def _col_binary_search(self, target, col, left, right):
        if left > right:
            return None

        if left == right:
            if col[left] == target:
                return left
            else:
                return None

        mid = left + (right - left) // 2
        if col[mid] == target:
            return mid
        elif col[mid] > target:
            return self._col_binary_search(target, col, left, mid - 1)
        elif col[mid] < target:
            return self._col_binary_search(target, col, mid + 1, right)


    def _row_binary_search(self, target, row, left, right):
        """
        :type row List[int]
        :type left int
        :type right int
        :type target int
        """
        if left > right:    # if input row is empty list
            return None

        if left == right:
            if row[left] > target:
                return None
            if row[left] < target:
                return left
#        if left < right:
#            return None
        mid = left + (right - left) // 2

        if row[mid] == target or row[mid] < target < row[mid + 1]:
            return mid
        elif target > row[mid]:
            return self._row_binary_search(target, row, mid + 1, right)
        elif target < row[mid]:
            return self._row_binary_search(target, row, left, mid - 1)


    def search_row(self, matrix, target):
        """
        :rtype: int: the row index that contains the target.
        """
        # property: the matrix[:return:] <= target
        row = [matrix[i][0] for i in range(len(matrix))]
        row_index = self._row_binary_search(target, row, 0, len(row) - 1)
        return row_index


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_index = self.search_row(matrix, target)
        if row_index is None:
            return False
        cols = matrix[row_index]
        col_index = self._col_binary_search(target, cols, 0, len(cols) - 1)
        return True if col_index is not None else False

if __name__ == '__main__':
    print(Solution().searchMatrix([[1, 3]], 3))