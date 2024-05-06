class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                end -= 1
                start += 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
