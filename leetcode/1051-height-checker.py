class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        order = sorted(heights)
        count = 0

        for i, j in zip(order, heights):
            if i != j:
                count += 1
        
        return count
