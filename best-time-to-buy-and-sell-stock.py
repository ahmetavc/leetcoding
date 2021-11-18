# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        maxProfitSoFar = 0
        buy = prices[0]
        
        for i in range(1, len(prices)):
            cur = prices[i]
            curProfit = cur - buy
            
            if curProfit < 0:
                buy = cur
                continue
                
            if curProfit > maxProfitSoFar:
                maxProfitSoFar = curProfit 
                
        return maxProfitSoFar
