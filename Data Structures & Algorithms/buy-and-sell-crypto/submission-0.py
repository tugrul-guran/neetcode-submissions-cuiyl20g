class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_profit = 0

        for i, current in enumerate(prices):
            for j in range(i, len(prices)):
                future = prices[j]
                profit = future - current

                best_profit = max(best_profit, profit)

        return best_profit