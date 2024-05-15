class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m * n - 1

        while start <= end:
            mid = (start + end) // 2
            row = mid // n
            col = mid - (n * row)

            val = matrix[row][col]

            if val == target:
                return True
            if val < target:
                start = mid + 1
            else:
                end = mid - 1
        
        return False
