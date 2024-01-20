def dfs(nums, picked, p, ps):
    if all(picked):
        ps.append(p)
        return
    
    for i in range(len(nums)):
        if not picked[i]:
            picked[i] = True
            dfs(nums, picked, p + [nums[i]], ps)
            picked[i] = False


class Solution:
    def permute(self, nums):
        permutations = []
        picked = [False for _ in range(len(nums))]

        for i in range(len(nums)):
            picked[i] = True
            dfs(nums, picked, [nums[i]], permutations)
            picked[i] = False
        
        return permutations
