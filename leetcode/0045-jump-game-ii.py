class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        max_len = nums[start]
        jump = 0
        n = len(nums)

        if n == 1:
            return 0

        while max_len < n - 1:
            local_max = max_len
            for i in range(start, max_len+1):
                if i + nums[i] > local_max:
                    local_max = i + nums[i]
                    k = i
            jump += 1
            max_len = local_max
            start = i
        
        return jump + 1
