class Solution(object):
    def maxProfit(self, prices):
        low = prices[0]
        profit = 0
        for i in prices:
            if low > i:
                low = i
            profit = max(i - low, profit)
        return profit
        