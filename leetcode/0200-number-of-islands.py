class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = [[0 for _ in range(cols)] for _ in range(rows)]
        islands = 0

        def dfs(row, col):
            if row < 0 or row > rows - 1:
                return 0
            if col < 0 or col > cols - 1:
                return 0
            if visit[row][col]:
                return 0
            if grid[row][col] == '0':
                return 0
            
            visit[row][col] = True

            for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs(row+r, col+c)
            
            return 1
        
        for row in range(rows):
            for col in range(cols):
                islands += dfs(row, col)

        return islands
