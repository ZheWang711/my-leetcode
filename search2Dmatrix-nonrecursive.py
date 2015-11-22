class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here

        #search the row
        lh = 0
        rh = len(matrix) - 1
        while rh > lh:
            # rh - lh >= 1
            mid = lh + (rh - lh + 1) // 2
            # mid >= lh + (2//2) = lh + 1
            # mid <= lh + (rh-lh+1)/ 2 = (rh +lh + 1 )/2  <= 2rh/2 = rh
            # lh <= mid < rh
            if matrix[mid][0] > target:
                rh = mid - 1
                # rh' = mid - 1 <= rh - 1 < rh
            elif matrix[mid][0] == target:
                return True
            else:
                lh = mid
                # lh' = mid >= lh + 1 > lh
        if rh < lh:
            return False
        else:
            row = rh    # row = rh = lh
            lh = 0
            rh = len(matrix[row]) - 1
            while rh > lh:
                mid = lh + (rh - lh) // 2
                if matrix[row][mid] > target:
                    rh = mid - 1
                elif matrix[row][mid] == target:
                    return True
                else:
                    lh = mid + 1
            if rh == lh and matrix[row][rh] == target:
                return True
            else:
                return False
