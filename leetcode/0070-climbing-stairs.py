class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2]

        if n < 3:
            return memo[n]

        for i in range(2, n):
            new_way = memo[1] + memo[2]
            memo[0] = memo[1]
            memo[1] = memo[2]
            memo[2] = new_way
        
        return memo[2]
