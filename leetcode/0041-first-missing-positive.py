class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = -abs(max(nums[i], 0))
        
        for n in nums:
            if n != 0 and abs(n) <= len(nums):
                if nums[abs(n)-1] == 0:
                    nums[abs(n)-1] = len(nums) + 1
                else:
                    nums[abs(n)-1] = abs(nums[abs(n)-1])

        for i in range(len(nums)):
            if nums[i] <= 0:
                return i + 1
        else:
            return len(nums) + 1