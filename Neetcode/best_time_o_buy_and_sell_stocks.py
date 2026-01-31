class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price_to_buy = float('inf')

        for price in prices:
            if price < min_price_to_buy:
                min_price_to_buy = price

            else:
                profit = price - min_price_to_buy
                max_profit = max(max_profit, profit)

        return max_profit
