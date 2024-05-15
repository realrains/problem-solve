class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def rsearch(start, end, target):
            while start <= end:
                mid = (start + end) // 2
                val = matrix[mid][0]
                if val == target:
                    return mid
                if val > target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return end

        def bsearch(start, end, row, value):
            while start <= end:
                mid = (start + end) // 2
                if row[mid] == value:
                    return True
                if row[mid] < value:
                    start = mid + 1
                else:
                    end = mid - 1
            return False

        row_idx = rsearch(0, len(matrix) - 1, target)
        row = matrix[row_idx]
        return bsearch(0, len(row) - 1, row, target)
