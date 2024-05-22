class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        move = ((1, 0), (0, 1), (-1, 0), (0, -1))
        direction = 0
        m = len(matrix)
        n = len(matrix[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        result = []
        x, y = 0, 0

        while (0 <= x < n) and (0 <= y < m) and not visit[y][x]:
            result.append(matrix[y][x])
            visit[y][x] = True

            dx, dy = move[direction]
            if (not (0 <= x + dx < n)) or (not (0 <= y + dy < m)) or visit[y+dy][x+dx]:
                direction = (direction + 1) % 4
            dx, dy = move[direction]
            
            x += dx
            y += dy
        
        return result
