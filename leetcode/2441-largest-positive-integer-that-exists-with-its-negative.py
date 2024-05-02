class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = [0] * 1000
        max_k = -1
        for num in nums:
            if count[abs(num)-1] != num:
                count[abs(num)-1] += num

            if count[abs(num)-1] == 0:
                max_k = max(abs(num), max_k)
        
        return max_k
