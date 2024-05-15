class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[-1]
        if n == 1:
            return max(nums[-1], nums[-2])

        dp = [0] * n
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-1], nums[-2])
        
        for i in reversed(range(len(nums)-2)):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])
        
        return dp[0]
