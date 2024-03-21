class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = [0 for _ in range(100)]

        for num in nums:
            counts[num-1] += 1
        
        max_freq = -1
        max_freq_cnt = 0

        for i in range(100):
            if counts[i] > max_freq:
                max_freq = counts[i]
                max_freq_cnt = 1
            elif counts[i] == max_freq:
                max_freq_cnt += 1
        
        return max_freq * max_freq_cnt
