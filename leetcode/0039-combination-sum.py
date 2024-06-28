class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = set()

        def getComb(selected, selectedSum):
            if selectedSum == target:
                results.add(tuple(sorted(selected)))
                return
            if selectedSum > target:
                return
            
            for candidate in candidates:
                getComb(selected + [candidate], selectedSum + candidate)
        
        getComb([], 0)

        return results
