class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        n = len(nums)

        if n == 0:
            return ranges
        
        start = nums[0]
        end = nums[0]

        for i in range(1, n):
            if nums[i] == end + 1:
                end += 1
            else:
                ranges.append(f'{start}->{end}' if start != end else str(start))
                start = nums[i]
                end = nums[i]
        else:
            ranges.append(f'{start}->{end}' if start != end else str(start))
        
        return ranges
        