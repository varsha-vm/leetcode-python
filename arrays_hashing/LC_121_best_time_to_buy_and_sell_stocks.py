#Approach: Min-so-far/Max-so-far
#Time: O(N)
#Space : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(profit, max_profit)

        return max_profit