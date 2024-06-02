class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        result = []
        finished = False

        for i in range(len(intervals)):
            start, end = intervals[i]

            if n_end < start and not finished:
                result.append([n_start, n_end])
                finished = True
                break
            elif n_start > end:
                result.append([start, end])
            elif n_start <= start and n_end >= end:
                continue
            elif n_start >= start and n_end <= end:
                finished = True
                break
            elif start <= n_start <= end:
                n_start = start
            elif start <= n_end <= end:
                n_end = end
        
        if finished:
            return result + intervals[i:]
        else:
            return result + [[n_start, n_end]]
