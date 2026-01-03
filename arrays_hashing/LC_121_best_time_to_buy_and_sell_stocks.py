#Approach: Min-so-far/Max-so-far => Greedy approach => Don't care about past to sell
#Time: O(N)
#Space : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            #Min-so-far
            if price < min_price:
                min_price = price

            #Max-so-far
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
            
        return max_profit