class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0
        nums.sort()
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= prev:
                result += (prev - nums[i]) + 1
                prev = prev + 1
            else:
                prev = nums[i]

        return result
