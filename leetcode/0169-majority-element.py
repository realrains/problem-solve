from typing import List

class Solution:
    # Boyer-Moore Majority Vote Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        major = None

        for num in nums:
            if count == 0:
                major = num
            if major == num:
                count += 1
            else:
                count -= 1
        
        return major

    # def majorityElement(self, nums: List[int]) -> int:
    #     counter = dict()
    #     for num in nums:
    #         if num in counter:
    #             counter[num] += 1
    #         else:
    #             counter[num] = 1
        
    #     for num, count in counter.items():
    #         if count > len(nums) // 2:
    #             return num