class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        delta = 1000
        counter = [0 for x in range(2001)]

        for n in arr:
            counter[n - delta] += 1
        
        occurs = list(filter(lambda s: s > 0, counter))

        return len(occurs) == len(set(occurs))
