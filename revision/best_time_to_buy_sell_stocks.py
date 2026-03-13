#Time: O(N)
#Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        buy_price = prices[0]
        output = 0

        
        for i in range(1, len(prices)):
            price = prices[i]
            #can we buy
            if price<buy_price:
                buy_price = price

            #if not can we sell
            else:
                profit = price - buy_price
                output = max(output, profit)

        return output