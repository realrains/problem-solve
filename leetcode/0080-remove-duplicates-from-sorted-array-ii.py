class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reader, writer, count = 0, 0, 0
        prev = None
        n = len(nums)
        while reader < n:
            if prev == nums[reader]:
                count += 1
            else:
                count = 1
            
            prev = nums[reader]
            
            if count >= 3:
                reader += 1
            else:
                nums[writer] = nums[reader]
                writer += 1
                reader += 1
        
        for _ in range(reader - writer):
            nums.pop()
