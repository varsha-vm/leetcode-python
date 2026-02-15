#Time : O(N)
#Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = float('inf')

        for price in prices:
            if price < buy_price:
                buy_price = price

            else:
                sell_price = price
                cur_profit = sell_price - buy_price
                max_profit = max(max_profit, cur_profit)

        return max_profit