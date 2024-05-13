class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        visit = [False] * n

        def backtrack(picked):
            if len(picked) == k:
                result.append(picked)
                return

            for i in range(n):
                if visit[i]:
                    continue
                if picked and picked[-1] < i+1:
                    continue
                visit[i] = True
                backtrack(picked + [i+1])
                visit[i] = False
        
        backtrack([])

        return result
