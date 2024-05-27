class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
        
        curr = 1

        for i in reversed(range(0, len(nums))):
            result[i] *= curr
            curr *= nums[i]
        
        return result
