class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0

        for price in prices:
            profit = max(profit, price - minBuy)
            minBuy = min(minBuy, price)
        
        return profit
