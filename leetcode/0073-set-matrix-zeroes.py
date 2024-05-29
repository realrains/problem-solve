class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        zero_row = False
        zero_col = False

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    if y > 0:
                        matrix[0][x] = 0
                    else:
                        zero_row = True

                    if x > 0:
                        matrix[y][0] = 0
                    else:
                        zero_col = True
        
        for y in range(1, m):
            for x in range(1, n):
                if matrix[0][x] == 0 or matrix[y][0] == 0:
                    matrix[y][x] = 0
        
        if zero_row:
            for x in range(n):
                matrix[0][x] = 0
        
        if zero_col:
            for y in range(m):
                matrix[y][0] = 0
