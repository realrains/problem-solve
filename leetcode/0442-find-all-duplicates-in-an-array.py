class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        return [k for k, v in counter.items() if v > 1]
