class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        n = len(citations)
        citations.sort()

        for i, e in enumerate(citations):
            if e >= n - i:
                h = max(h, n - i)

        return h
