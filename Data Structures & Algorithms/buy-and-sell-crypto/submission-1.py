class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        best_profit = 0

        lowest_seen = prices[0]

        for i in range(1, len(prices)):

            sell_price = prices[i] - lowest_seen

            best_profit = max(best_profit, sell_price)

            if prices[i] < lowest_seen:
                lowest_seen = prices[i]

        return best_profit