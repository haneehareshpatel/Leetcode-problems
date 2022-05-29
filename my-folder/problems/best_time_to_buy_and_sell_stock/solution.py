class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        min_price=prices[0]
        for x in range(1,len(prices)):
            if prices[x]-min_price>maxprofit:
                maxprofit=prices[x]-min_price
            if prices[x]<min_price:
                min_price=prices[x]
        return maxprofit