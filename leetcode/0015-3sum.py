class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = set()
        nums = sorted(nums)

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                triple = (nums[i], nums[j], nums[k])
                s = sum(triple)
                if s == 0:
                    triples.add(triple)
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1 
        
        return list(triples)
