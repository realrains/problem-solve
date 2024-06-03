class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1

        def swap(x, y):
            cx, cy = x, y
            prev = -1

            for _ in range(5):
                nx, ny = cy, n-cx
                temp = matrix[cx][cy]
                matrix[cx][cy] = prev
                prev = temp
                cx, cy = nx, ny
        
        for i in range(n):
            for j in range(i, n-i):
                swap(i, j)
