class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = len(nums) + 1
        start = 0
        end = 0
        summation = nums[0]

        while start <= end:
            if summation >= target:
                minimum = min(minimum, end - start + 1)
                summation -= nums[start]
                start += 1
                
            else:
                end += 1
                if end >= len(nums):
                    break
                summation += nums[end]

        return 0 if minimum > len(nums) else minimum
