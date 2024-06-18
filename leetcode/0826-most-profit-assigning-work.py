class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp = sorted([[d, p] for d, p in zip(difficulty, profit)])

        max_profit = 0

        worker.sort()

        last_job = 0
        workers_max = 0
        for w in worker:
            for i in range(last_job, len(dp)):
                d, p = dp[i]
                if d <= w:
                    if workers_max < p:
                        workers_max = p
                    last_job = i
                else:
                    break
            max_profit += workers_max

        return max_profit
