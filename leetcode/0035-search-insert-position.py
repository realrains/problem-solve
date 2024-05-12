class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)

        while start < end:
            mid = ((start + end) // 2)
            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        
        return start
