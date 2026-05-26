from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Two pointer
        start = 0
        i = 1
        profit = 0
        while i < len(prices):
            temp = prices[i] - prices[start]
            if temp > 0:
                profit = max(profit, temp)
            else:
                start = i
            
            i+=1 
        
        return profit

        # other

        # maxProfit = 0
        # minPrice = prices[0]
        # for price in prices:
        #     maxProfit = max(maxProfit, price - minPrice)
        #     minPrice = min(price, minPrice)
        
        # return maxProfit


# Time complexity: O(n)
# Space complexity: O(1)