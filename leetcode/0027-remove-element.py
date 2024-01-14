class Solution:
    def removeElement(self, nums, val):
        m = len(nums) - 1

        while m >= 0 and nums[m] == val:
            m -= 1
        
        s = 0

        while s < m:
            if nums[s] == val:
                nums[s], nums[m] = nums[m], nums[s]
                while m >= 0 and nums[m] == val:
                    m -= 1
            s += 1

        return len(nums) - nums.count(val)