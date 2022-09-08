class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for x in range(1,len(dp)):
            for y in coins:
                if x-y >=0:
                    dp[x]=min(dp[x],1+dp[x-y])
        if dp[amount]!=amount+1:
            return dp[amount]
        else:
            return -1