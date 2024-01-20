from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    zeros.append((y, x))
        
        for y, x in zeros:
            self.set_row(y, matrix)
            self.set_col(x, matrix)
    
    def set_row(self, y, matrix):
        for x in range(len(matrix[0])):
            matrix[y][x] = 0
    
    def set_col(self, x, matrix):
        for y in range(len(matrix)):
            matrix[y][x] = 0
