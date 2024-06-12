class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0, 0, 0]

        for num in nums:
            counter[num] += 1
        
        for i in range(len(nums)):
            if counter[0] > 0:
                counter[0] -= 1
                nums[i] = 0
            elif counter[1] > 0:
                counter[1] -= 1
                nums[i] = 1
            elif counter[2] > 0:
                counter[2] -= 1
                nums[i] = 2
