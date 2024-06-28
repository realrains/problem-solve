class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dp = [[-1] * cols for _ in range(rows)]
        dp[rows-1][cols-1] = grid[rows-1][cols-1]

        def dynamic(row, col):
            if dp[row][col] >= 0:
                return dp[row][col]
            
            result = []
            if row < rows-1:
                result.append(dynamic(row+1, col))
            
            if col < cols-1:
                result.append(dynamic(row, col+1))
            
            dp[row][col] = min(result) + grid[row][col]
            return dp[row][col]
        
        return dynamic(0, 0)
