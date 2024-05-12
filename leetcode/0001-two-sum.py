class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_nums = list(enumerate(nums))
        idx_nums.sort(key=lambda e: e[1])
        i, j = 0, len(nums)-1

        while i < j:
            s = idx_nums[i][1] + idx_nums[j][1]

            if s == target:
                return [idx_nums[i][0], idx_nums[j][0]]

            if s < target:
                i += 1
            else:
                j -= 1
