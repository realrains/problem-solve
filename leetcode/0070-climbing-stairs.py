class Solution:
    def __init__(self):
        self.dp = [0 for _ in range(46)]
        self.dp[0] = 1
        self.dp[1] = 1

    def climbStairs(self, n: int) -> int:
        if self.dp[n] != 0:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        