class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_price = 0
        i = 0
        max_profit = 0

        while i < len(prices):
            if prices[i] < min_price:
                min_price = prices[i]
                max_price = min_price
            if prices[i] > max_price:
                max_price = prices[i]

            max_profit = max(max_profit, max_price - min_price)
            i += 1
        
        return max_profit
