class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0]
        result = []

        for i in range(1, len(intervals)):
            s, e = intervals[i]

            if s <= end:
                end = max(e, end)
            else:
                result.append([start, end])
                start = s
                end = e
        
        result.append([start, end])
        
        return result
