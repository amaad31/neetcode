class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = r = 0
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
            else:
                max_profit = max(max_profit, curr_profit)
            r += 1
        return max_profit