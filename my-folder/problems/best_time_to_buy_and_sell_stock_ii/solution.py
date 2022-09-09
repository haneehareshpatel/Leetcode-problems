class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        
        for x in range(1,len(prices)):
            if prices[x]>prices[x-1]:
                maxprofit +=prices[x]-prices[x-1]
        return maxprofit