class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader, writer = 0, 0
        n = len(nums)
        last = None

        while writer < n and reader < n:
            if nums[reader] == last:
                reader += 1
            else:
                nums[writer] = nums[reader]
                last = nums[reader]
                writer += 1
                reader += 1
        
        return writer
