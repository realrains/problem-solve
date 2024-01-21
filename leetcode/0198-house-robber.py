from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1 for _ in range(len(nums))]

        def recursive(n):
            if n >= len(nums):
                return 0
            if dp[n] > 0:
                return dp[n]
            dp[n] = nums[n] + max(recursive(n+2), recursive(n+3))
            return dp[n]

        for i in range(len(nums)):
            recursive(i)

        return max(dp)

        