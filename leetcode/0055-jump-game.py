class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = [None for _ in range(n)]
        memo[n-1] = True

        def can(x):
            if memo[x] is not None:
                return memo[x]

            delta = nums[x]

            if delta == 0:
                memo[x] = False
                return False
            
            if x + delta >= n - 1:
                memo[x] = True
                return True
            
            for i in range(delta):
                if x + i + 1 < n and can(x+i+1):
                    memo[x] = True
                    return True

            memo[x] = False
            return False
        
        return can(0)
